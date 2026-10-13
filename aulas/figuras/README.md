# Figuras das aulas

Os esquemas são escritos em LaTeX/TikZ, com o estilo comum de
`fontes/estilo.tex`. As cores acompanham a identidade visual das aulas;
as fontes matemáticas são Latin Modern. O material autoral segue a licença
CC BY 4.0 do repositório, com atribuição ao Prof. Diego Volpatto.

- `fontes/` contém os arquivos editáveis.
- `geradas/` contém os SVG usados nas apresentações e os PDF vetoriais para reutilização.

As apresentações usam os SVG já incluídos no repositório. Não é necessário
instalar LaTeX para abrir as aulas ou gerar o HTML.

Para recompilar os esquemas, use uma instalação de TeX Live ou MacTeX com
TikZ e `standalone`, além de Poppler (`pdftocairo`), disponíveis no `PATH`:

```sh
pixi run figuras
pixi run aulas
```

O comando guarda arquivos intermediários em `.validacao/figuras/`, fora do
Git. Confira as figuras após modificar textos, setas ou dimensões: compilar
sem erros não garante que rótulos e elementos estejam bem posicionados.

Nos fluxogramas, os nós são posicionados em relação às bordas dos anteriores.
A macro `\verificarsetadireita` recusa ligações horizontais com menos de
4 mm de espaço, evitando inversões involuntárias após mudanças no texto.

Nos slides, use uma descrição acessível sem gerar uma legenda redundante:

```markdown
![](figuras/geradas/07-malha-e-atributos.svg){.diagrama fig-alt="Descrição da figura."}
```
