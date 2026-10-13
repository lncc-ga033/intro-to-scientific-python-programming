"""Compila os esquemas TikZ das aulas em PDF e SVG."""

import shutil
import subprocess
from pathlib import Path

RAIZ = Path(__file__).resolve().parents[1]
FONTES = RAIZ / "aulas" / "figuras" / "fontes"
DESTINO = RAIZ / "aulas" / "figuras" / "geradas"
TEMPORARIOS = RAIZ / ".validacao" / "figuras"


def gerar():
    """Mantém a geração separada das aulas, que usam os SVG já disponíveis."""
    for ferramenta in ("pdflatex", "pdftocairo"):
        if shutil.which(ferramenta) is None:
            raise SystemExit(f"Ferramenta necessária para recompilar figuras: {ferramenta}.")
    DESTINO.mkdir(parents=True, exist_ok=True)
    for fonte in sorted(FONTES.glob("[0-9]*.tex")):
        trabalho = TEMPORARIOS / fonte.stem
        trabalho.mkdir(parents=True, exist_ok=True)
        compilacao = subprocess.run(
            [
                "pdflatex", "-halt-on-error", "-interaction=nonstopmode",
                f"-output-directory={trabalho}", fonte.name,
            ],
            cwd=FONTES, capture_output=True, text=True,
        )
        if compilacao.returncode:
            raise RuntimeError(f"Falha em {fonte.name}:\n{compilacao.stdout[-5000:]}")
        log = (trabalho / f"{fonte.stem}.log").read_text()
        if "Overfull" in log or "Missing character" in log:
            raise RuntimeError(f"Revise o log antes de publicar a figura: {trabalho}.")
        pdf = trabalho / f"{fonte.stem}.pdf"
        svg = DESTINO / f"{fonte.stem}.svg"
        subprocess.run(
            ["pdftocairo", "-svg", str(pdf), str(svg)],
            check=True, capture_output=True, text=True,
        )
        shutil.copy2(pdf, DESTINO / pdf.name)
        print(f"Gerado: {fonte.stem} (PDF e SVG).")


if __name__ == "__main__":
    gerar()
