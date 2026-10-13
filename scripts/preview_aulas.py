"""Abre a prévia das aulas, liberando prévias anteriores e escolhendo uma porta."""

import argparse
import os
import re
import shutil
import signal
import socket
import subprocess
import sys
from pathlib import Path

import psutil

RAIZ = Path(__file__).resolve().parents[1]
HOST = "127.0.0.1"
ANSI = re.compile(r"\x1b\[[0-?]*[ -/]*[@-~]")
PORTA_OCUPADA = re.compile(
    r"Requested port \d+ is already in use\.|AddrInUse|Address already in use|"
    r"Only one usage of each socket address",
    re.IGNORECASE,
)
ENDERECO = re.compile(r"(?:Listening on|Browse at)\s+(https?://\S+)")


def caminho_absoluto(caminho, diretorio):
    """Resolve um argumento de comando a partir do diretório do processo."""
    caminho = Path(caminho)
    return (caminho if caminho.is_absolute() else Path(diretorio) / caminho).resolve()


def previa_do_projeto(comando, diretorio, raiz=RAIZ):
    """Reconhece o launcher ou um Quarto preview cujo alvo é exatamente aulas/."""
    if not comando or not diretorio:
        return False
    executavel = Path(comando[0]).name.lower()
    if executavel.startswith("python") and len(comando) > 1:
        script = caminho_absoluto(comando[1], diretorio)
        return script == raiz / "scripts" / "preview_aulas.py"
    if executavel in {"quarto", "quarto.exe"}:
        argumentos = comando[1:]
    elif executavel in {"bash", "sh"} and len(comando) > 1:
        if Path(comando[1]).name != "quarto":
            return False
        argumentos = comando[2:]
    elif executavel in {"deno", "deno.exe"}:
        indices = [i for i, valor in enumerate(comando) if Path(valor).name == "quarto.js"]
        if not indices:
            return False
        argumentos = comando[indices[0] + 1 :]
    else:
        return False
    if not argumentos or argumentos[0] != "preview":
        return False
    alvo = argumentos[1] if len(argumentos) > 1 else "."
    if alvo.startswith("-"):
        # Sem um alvo explícito na primeira posição, não há identidade suficiente.
        return False
    return caminho_absoluto(alvo, diretorio) == raiz / "aulas"


def encerrar_processos(processos, grupos=()):
    """Encerra os processos identificados e seus filhos, conferindo identidade de PID."""
    arvore = {}
    for processo in processos:
        arvore[processo.pid] = processo
        try:
            for filho in processo.children(recursive=True):
                arvore[filho.pid] = filho
        except psutil.Error:
            continue
    grupos = set(grupos)
    for processo in arvore.values():
        try:
            processo.terminate()
        except psutil.Error:
            pass
    for grupo in grupos:
        try:
            os.killpg(grupo, signal.SIGTERM)
        except (ProcessLookupError, PermissionError):
            pass
    _, restantes = psutil.wait_procs(list(arvore.values()), timeout=3)
    for grupo in grupos:
        try:
            os.killpg(grupo, signal.SIGKILL)
        except (ProcessLookupError, PermissionError):
            pass
    for processo in restantes:
        try:
            processo.kill()
        except psutil.Error:
            pass
    psutil.wait_procs(restantes, timeout=3)


def fechar_previas(raiz=RAIZ):
    """Libera apenas prévias comprovadamente pertencentes a este projeto."""
    atual = psutil.Process()
    protegidos = {atual.pid, *(processo.pid for processo in atual.parents())}
    anteriores = []
    for processo in psutil.process_iter(["cmdline", "cwd"]):
        if processo.pid in protegidos:
            continue
        try:
            if previa_do_projeto(processo.info["cmdline"], processo.info["cwd"], raiz):
                anteriores.append(processo)
        except (OSError, psutil.Error):
            continue
    if anteriores:
        print("Encerrando prévias anteriores deste projeto...", flush=True)
        encerrar_processos(anteriores)
    return bool(anteriores)


def escolher_porta(preferida):
    """Tenta a porta preferida e as seguintes; em último caso, pede uma ao sistema."""
    for porta in range(preferida, min(preferida + 100, 65536)):
        with socket.socket() as servidor:
            try:
                servidor.bind((HOST, porta))
                servidor.listen(1)
            except OSError:
                continue
            return porta
    with socket.socket() as servidor:
        servidor.bind((HOST, 0))
        return servidor.getsockname()[1]


def executar_previa(quarto, porta, raiz=RAIZ):
    """Repasse a saída e retorne a indicação de uma corrida pela porta."""
    # O lock do Quarto contém só um PID e faria o próprio Quarto encerrar outra
    # prévia sem verificar se o PID ainda pertence ao projeto.
    # A identificação acima é a responsável pelo encerramento dos processos.
    (raiz / "aulas" / ".quarto" / "preview" / "lock").unlink(missing_ok=True)
    opcoes = (
        {"creationflags": subprocess.CREATE_NEW_PROCESS_GROUP}
        if os.name == "nt"
        else {"start_new_session": True}
    )
    processo = subprocess.Popen(
        [
            quarto,
            "preview",
            str(raiz / "aulas"),
            "--host",
            HOST,
            "--port",
            str(porta),
            "--no-browser",
        ],
        cwd=raiz,
        stdout=subprocess.PIPE,
        stderr=subprocess.STDOUT,
        text=True,
        encoding="utf-8",
        errors="replace",
        bufsize=1,
        **opcoes,
    )
    conhecidos = {}
    try:
        gerenciado = psutil.Process(processo.pid)
        conhecidos[gerenciado.pid] = gerenciado
    except psutil.NoSuchProcess:
        gerenciado = None
    ocupada = False
    endereco_mostrado = False
    try:
        for linha in processo.stdout:
            if gerenciado:
                try:
                    for filho in gerenciado.children(recursive=True):
                        conhecidos[filho.pid] = filho
                except psutil.Error:
                    pass
            texto = ANSI.sub("", linha)
            if PORTA_OCUPADA.search(texto):
                ocupada = True
            if ocupada:
                continue
            print(linha, end="", flush=True)
            endereco = ENDERECO.search(texto)
            if endereco and not endereco_mostrado:
                print(f"\nAbra as aulas em: {endereco.group(1)}\n", flush=True)
                endereco_mostrado = True
        return processo.wait(), ocupada
    finally:
        grupos = [processo.pid] if os.name != "nt" else []
        encerrar_processos(conhecidos.values(), grupos)
        processo.wait()
        processo.stdout.close()


def porta_valida(valor):
    porta = int(valor)
    if not 1 <= porta <= 65535:
        raise argparse.ArgumentTypeError("A porta deve estar entre 1 e 65535.")
    return porta


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--porta", type=porta_valida, default=8766, help="Porta preferida (8766).")
    parser.add_argument(
        "--fechar-anteriores",
        action="store_true",
        default=True,
        help="Encerra prévias deste projeto antes de abrir outra (padrão: ativado).",
    )
    parser.add_argument(
        "--encerrar", action="store_true", help="Encerra todas as prévias do projeto."
    )
    argumentos = parser.parse_args()
    if argumentos.encerrar:
        fechar_previas()
        print("Prévias deste projeto encerradas.", flush=True)
        return 0
    quarto = shutil.which("quarto")
    if not quarto:
        parser.error("Quarto não encontrado. Execute pelo ambiente Pixi.")

    def interromper(_sinal, _frame):
        raise KeyboardInterrupt

    signal.signal(signal.SIGTERM, interromper)
    if os.name == "nt":
        signal.signal(signal.SIGBREAK, interromper)
    try:
        fechar_previas()
        preferida = argumentos.porta
        for _ in range(5):
            porta = escolher_porta(preferida)
            if porta != preferida:
                print(f"A porta {preferida} está ocupada; usando a porta {porta}.", flush=True)
            print("Preparando a prévia das aulas...", flush=True)
            retorno, ocupada = executar_previa(quarto, porta)
            if not ocupada:
                return retorno
            print(
                f"A porta {porta} foi ocupada durante a inicialização; tentando outra.", flush=True
            )
            preferida = porta + 1 if porta < 65535 else 8766
        print("Não foi possível iniciar a prévia após cinco tentativas.", file=sys.stderr)
        return 1
    except KeyboardInterrupt:
        print("\nPrévia encerrada.", flush=True)
        return 0
    except OSError as erro:
        print(f"Não foi possível abrir a prévia: {erro}", file=sys.stderr)
        return 1


if __name__ == "__main__":
    sys.exit(main())
