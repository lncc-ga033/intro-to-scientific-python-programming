"""Disponibiliza nas aulas uma cópia gerada do pacote usado pelo Pyodide."""

import shutil
from pathlib import Path

RAIZ = Path(__file__).resolve().parents[1]


def preparar():
    """Copia somente fontes Python; src/malhalib continua sendo a fonte editável."""
    origem = RAIZ / "src" / "malhalib"
    destino = RAIZ / "aulas" / "malhalib"
    if not origem.is_dir():
        raise FileNotFoundError(f"Pacote não encontrado em {origem}.")
    if destino.exists():
        shutil.rmtree(destino)
    shutil.copytree(origem, destino, ignore=shutil.ignore_patterns("__pycache__", "*.pyc"))
    suplementos = RAIZ / "aulas" / "suplementos"
    if suplementos.exists():
        shutil.rmtree(suplementos)
    for nome in ("notebooks", "docs"):
        shutil.copytree(
            RAIZ / nome,
            suplementos / nome,
            ignore=shutil.ignore_patterns("__pycache__", ".ipynb_checkpoints"),
        )
    print("Preparado: malhalib para execução no navegador.")


if __name__ == "__main__":
    preparar()
