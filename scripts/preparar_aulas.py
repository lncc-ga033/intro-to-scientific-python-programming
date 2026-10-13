"""Prepara os suplementos e os recursos da versão web das aulas."""

import argparse
import os
import shutil
from pathlib import Path

RAIZ = Path(__file__).resolve().parents[1]


def publicar_suplementos():
    """Inclui os notebooks e documentos somente no artefato web gerado."""
    saida = Path(os.environ.get("QUARTO_PROJECT_OUTPUT_DIR", RAIZ / "aulas" / "_site"))
    suplementos = saida / "suplementos"
    if suplementos.exists():
        shutil.rmtree(suplementos)
    for nome in ("notebooks", "docs"):
        shutil.copytree(
            RAIZ / nome,
            suplementos / nome,
            ignore=shutil.ignore_patterns("__pycache__", ".ipynb_checkpoints"),
        )
    print("Preparados: materiais suplementares na versão web gerada.")


def publicar_pacote():
    """Inclui as fontes de src/malhalib somente no artefato web gerado."""
    origem = RAIZ / "src" / "malhalib"
    if not origem.is_dir():
        raise FileNotFoundError(f"Pacote não encontrado em {origem}.")
    saida = Path(os.environ.get("QUARTO_PROJECT_OUTPUT_DIR", RAIZ / "aulas" / "_site"))
    destino = saida / "malhalib"
    if destino.exists():
        shutil.rmtree(destino)
    shutil.copytree(origem, destino, ignore=shutil.ignore_patterns("__pycache__", "*.pyc"))
    print("Preparado: malhalib na versão web gerada.")


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--publicar-pacote", action="store_true")
    argumentos = parser.parse_args()
    if argumentos.publicar_pacote:
        publicar_pacote()
    else:
        publicar_pacote()
        publicar_suplementos()
