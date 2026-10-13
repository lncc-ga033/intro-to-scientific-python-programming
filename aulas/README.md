# Aulas interativas da GA033

**Prof. Diego Volpatto**

Programa de Pós-Graduação em Modelagem Computacional · LNCC

As nove apresentações acompanham o percurso dos notebooks. Cada slide
introduz um conceito e um exemplo curto; os cadernos oferecem explicações
adicionais e exercícios para estudo.

## Abrir e apresentar

Na raiz do repositório:

```sh
pixi install --locked
pixi run aulas-preview
```

Abra `http://127.0.0.1:8766/`. Escolha uma aula no índice e use as setas.
Clique no código para editar e em **Executar** para avaliar. **Restaurar
código** recupera o exemplo original. O botão restaura o texto da célula;
para reiniciar todo o ambiente Python do navegador, recarregue a página.

A primeira abertura carrega o Python e as bibliotecas pela internet.
Os exemplos usam o ambiente do navegador; os comandos de terminal são
demonstrados no ambiente local. Para guardar experimentos, use os notebooks
no JupyterLab: `pixi run lab`.

Para projetar, abra a aula em uma janela ampla ou em tela cheia. Use **Esc**
para uma visão geral dos slides e **S** para abrir as notas do apresentador.
O menu no canto inferior esquerdo permite ir diretamente a um assunto.

## Editar

- Os arquivos `.qmd` são as fontes editáveis das apresentações.
- `_quarto.yml` reúne a identidade visual, a autoria, a filiação e as opções comuns.
- `assets/lncc.scss` define cores, tipografia e espaço para código e resultados.
- `assets/interacao.js` traduz os controles e preserva a navegação enquanto o editor tem foco.
- `src/malhalib/`, na raiz do projeto, é a fonte única do pacote usado na aula 07.

As células usam blocos `{pyodide}`. Mantenha cada exemplo independente:
declare seus dados e imports no mesmo slide. Use `.plot-slide` nos títulos
dos slides que mostram editor e gráfico lado a lado. Use `.output-columns`
para código e saídas textuais mais extensas. Prefira encurtar um
exemplo ou dividir o assunto a reduzir a fonte ou sobrecarregar o slide.

O corpo fica centralizado verticalmente em uma área delimitada. O cabeçalho
e o rodapé ficam fora dessa área; quando uma edição aumenta demais o corpo,
a rolagem ocorre somente dentro dele. Esse limite protege a diagramação,
mas não substitui a revisão visual após editar ou executar os exemplos.

## Gerar e verificar

```sh
pixi run aulas-verificar
pixi run aulas
pixi run aulas-servir
```

`aulas-verificar` executa cada bloco em um namespace novo no Python local.
Essa verificação deve ser complementada pela execução no navegador, que usa
um ambiente diferente, e pela revisão visual dos slides.

A geração prepara cópias dos materiais suplementares e de `malhalib` para
distribuição. `aulas/malhalib/`, `aulas/suplementos/`, `.quarto/` e `_site/`
são pastas geradas e ficam fora do Git. Edite os originais em `src/`, `docs/`
e `notebooks/`. Para compartilhar a versão web, use todo o conteúdo de
`aulas/_site/`, incluindo as bibliotecas e os recursos.

Licença do material autoral: [CC BY 4.0](../LICENSE), com atribuição a
Diego Tavares Volpatto. As ferramentas e os materiais de terceiros conservam
suas próprias licenças.
