"""Exporta as saídas já salvas dos notebooks para leitura no navegador."""

import re
from pathlib import Path

import nbformat
from nbconvert import HTMLExporter

RAIZ = Path(__file__).resolve().parents[1]


def exportar():
    destino = RAIZ / "resultados" / "html"
    destino.mkdir(parents=True, exist_ok=True)
    exportador = HTMLExporter(template_name="lab")
    for arquivo in sorted((RAIZ / "notebooks").glob("*.ipynb")):
        caderno = nbformat.read(arquivo, as_version=4)
        for celula in caderno.cells:
            if celula.cell_type == "markdown":
                # Os cadernos exportados ficam um nível abaixo dos originais.
                celula.source = re.sub(
                    r"\]\(([^)]+)\.ipynb(#[^)]*)?\)",
                    lambda m: (
                        m[0] if "://" in m[1] else f"]({Path(m[1]).name}.html{m[2] or ''})"
                    ),
                    celula.source,
                )
                celula.source = celula.source.replace("](../", "](../../")
        corpo, _ = exportador.from_notebook_node(caderno)
        (destino / f"{arquivo.stem}.html").write_text(corpo, encoding="utf-8")
        print(f"Exportado: {arquivo.stem}.html")


if __name__ == "__main__":
    exportar()
