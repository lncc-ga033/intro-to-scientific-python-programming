"""Verifica se os exemplos das aulas executam sem depender de outros slides."""

import contextlib
import io
import re
from pathlib import Path

import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt  # noqa: E402

RAIZ = Path(__file__).resolve().parents[1]
BLOCO_PYTHON = re.compile(r"^```\{pyodide\}\n(.*?)^```", re.MULTILINE | re.DOTALL)


def verificar():
    """Executa cada bloco em um namespace novo no Python do ambiente Pixi."""
    total = 0
    arquivos = sorted((RAIZ / "aulas").glob("[0-9]*.qmd"))
    if not arquivos:
        raise RuntimeError("Nenhuma aula encontrada.")
    for arquivo in arquivos:
        texto = arquivo.read_text(encoding="utf-8")
        if chr(0x2014) in texto:
            raise ValueError(f"Use -- no lugar do travessão em {arquivo.name}.")
        blocos = BLOCO_PYTHON.findall(texto)
        for indice, bloco in enumerate(blocos, start=1):
            codigo = "\n".join(linha for linha in bloco.splitlines() if not linha.startswith("#|"))
            namespace = {"__name__": "__main__"}
            try:
                with contextlib.redirect_stdout(io.StringIO()):
                    exec(compile(codigo, f"{arquivo.name}:bloco{indice}", "exec"), namespace)
            except Exception as erro:
                raise RuntimeError(f"Falha em {arquivo.name}, bloco {indice}.") from erro
            finally:
                plt.close("all")
        total += len(blocos)
        print(f"OK: {arquivo.name} -- {len(blocos)} blocos independentes", flush=True)
    print(f"Verificadas {len(arquivos)} aulas e {total} blocos no Python local.")
    print("Confira também a execução Pyodide e o layout no navegador.")


if __name__ == "__main__":
    verificar()
