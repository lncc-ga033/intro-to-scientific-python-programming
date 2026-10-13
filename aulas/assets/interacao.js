/* Tradução dos controles do Quarto Live, sem modificar a extensão vendorizada. */
(() => {
  const traducoes = new Map([
    ["Run Code", "Executar"], ["Start Over", "Restaurar código"],
    ["Python Code", "Código Python"],
    ["Show Hint", "Mostrar dica"], ["Show Solution", "Mostrar solução"],
    ["Initialise", "Preparando Python"],
    ["Downloading Pyodide", "Carregando Python no navegador"],
    ["Pyodide environment setup", "Preparando o ambiente Python"],
  ]);
  function traduzir() {
    document.querySelectorAll(".exercise-editor .card-header, .exercise-loading-details").forEach(el => {
      const nos = document.createTreeWalker(el, NodeFilter.SHOW_TEXT);
      let no;
      while ((no = nos.nextNode())) {
        const texto = no.textContent.trim();
        const traducao = traducoes.get(texto)
          || (texto.startsWith("Downloading package: ") ? texto.replace("Downloading package: ", "Carregando biblioteca: ") : null)
          || (texto.startsWith("Downloading resource: ") ? texto.replace("Downloading resource: ", "Carregando arquivo: ") : null);
        if (traducao) no.textContent = traducao;
      }
    });
    document.querySelectorAll(".btn-exercise-editor").forEach(el => {
      el.setAttribute("aria-label", el.textContent.trim());
    });
  }
  document.addEventListener("DOMContentLoaded", () => {
    traduzir();
    new MutationObserver(traduzir).observe(document.body, {
      childList: true, subtree: true, characterData: true,
    });
    // O editor recebe suas teclas; Reveal só navega quando o foco está fora dele.
    if (window.Reveal) {
      window.Reveal.configure({
        keyboardCondition: evento => !evento.target.closest(
          ".cm-editor, input, textarea, select, [contenteditable]"
        ),
      });
    }
  });
})();
