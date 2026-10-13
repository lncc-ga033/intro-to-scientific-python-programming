# Cabeçalho LNCC para materiais Quarto

**Prof. Diego Volpatto**

Programa de Pós-Graduação em Modelagem Computacional · LNCC

O template coloca o logo à esquerda do título, no mesmo espaço horizontal
do cabeçalho. Os dois ficam alinhados pelo centro na direção vertical.
Autoria e filiação permanecem abaixo. O logo conserva suas proporções e
tem uma descrição acessível, sem legenda repetida.

## Usar neste projeto

No cabeçalho YAML de um documento `.qmd` localizado em `aulas/`:

```yaml
title: "Título do material"
lncc-logo: assets/lncc.png
lncc-logo-alt: Laboratório Nacional de Computação Científica
format:
  html:
    theme: cosmo
    css:
      - templates/lncc/cabecalho.css
    template-partials:
      - templates/lncc/title-block.html
```

Se o documento já usa outro arquivo CSS, mantenha-o na lista `css`.
O título, o subtítulo opcional, a autoria e a filiação são definidos nos
metadados habituais do Quarto. A implementação conserva a estrutura nativa
do bloco de título e usa o template de metadados do próprio Quarto.

## Reutilizar em outro projeto

1. Copie `title-block.html`, `cabecalho.css` e `modelo.qmd` para uma pasta do novo projeto.
2. Copie o logo original para os recursos do projeto e ajuste `lncc-logo` no modelo.
3. Ajuste título, subtítulo, autoria e filiação e renderize o arquivo com Quarto.

Os caminhos são relativos ao arquivo `.qmd`. O [modelo](modelo.qmd) pode
ser renderizado nesta pasta; ao copiá-lo, atualize o caminho do logo.
Não há dependência de JavaScript para posicionar o cabeçalho.

O logo tem largura padrão de 180 px. Para ajustar o tamanho ou o espaçamento,
sobrescreva `--lncc-logo-width` e `--lncc-header-gap` no CSS do novo material.
Em telas estreitas, essas medidas e a fonte do título diminuem, mantendo o
logo à esquerda, o alinhamento vertical e a quebra de linhas do texto.

O template se aplica a documentos HTML. As apresentações Reveal.js usam
o tema `assets/lncc.scss`.

Referência técnica: [templates parciais do Quarto](https://quarto.org/docs/journals/templates.html#html-partials).

O código autoral segue a licença [CC BY 4.0](../../../LICENSE), com atribuição
a Diego Tavares Volpatto. O logo mantém suas condições de uso institucionais.
