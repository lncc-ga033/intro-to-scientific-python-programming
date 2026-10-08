"""Executa cada notebook em um kernel novo e em uma cópia temporária do curso."""

import argparse
import shutil
import tempfile
from pathlib import Path

import nbformat
from nbclient import NotebookClient

RAIZ = Path(__file__).resolve().parents[1]


def verificar(gravar=False):
    """Verifica execução sequencial, sem aproveitar estado de outro notebook."""
    arquivos = sorted((RAIZ / "notebooks").glob("*.ipynb"))
    if not arquivos:
        raise RuntimeError("Nenhum notebook encontrado.")
    with tempfile.TemporaryDirectory(prefix="ga033-") as pasta:
        copia = Path(pasta)
        for nome in ("notebooks", "exemplos"):
            shutil.copytree(RAIZ / nome, copia / nome)
        # O manifesto também identifica a raiz nos exemplos de caminhos relativos.
        shutil.copy2(RAIZ / "pixi.toml", copia / "pixi.toml")
        for arquivo in arquivos:
            caderno = nbformat.read(arquivo, as_version=4)
            nbformat.validate(caderno)
            cliente = NotebookClient(
                caderno,
                timeout=120,
                kernel_name="python3",
                allow_errors=False,
                resources={"metadata": {"path": str(copia / "notebooks")}},
            )
            cliente.execute()
            if gravar:
                nbformat.write(caderno, arquivo)
            quantidade = sum(c.cell_type == "code" for c in caderno.cells)
            print(f"OK: {arquivo.name} -- {quantidade} células de código", flush=True)
    print(f"Verificados {len(arquivos)} notebooks em kernels independentes.")


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--gravar", action="store_true", help="Salva as saídas nos notebooks.")
    verificar(parser.parse_args().gravar)
