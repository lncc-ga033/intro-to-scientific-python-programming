# Introdução à programação científica com Python

**Um crash course que integra a disciplina GA033 - Método de Elementos Finitos: Implementação Computacional, do LNCC.**

**Prof. Diego Volpatto**

Programa de Pós-Graduação em Modelagem Computacional · LNCC

**Idioma:** Português brasileiro (PT-BR) · **Licença:** CC BY 4.0

Este módulo prepara os participantes da [GA033](https://lncc-ga033.github.io/) para escrever, executar, compreender e organizar programas científicos em Python. O material parte dos fundamentos da linguagem e acompanha a construção gradual das habilidades necessárias às atividades computacionais da disciplina.

Não é necessário conhecer Python. Utilizamos aritmética e noções de funções; os cadernos sobre sistemas lineares pressupõem conhecimentos básicos de vetores e matrizes. A prática é parte da aula: executar, prever resultados, modificar exemplos e explicar o que mudou.

## Aulas interativas e material suplementar

As apresentações em [`aulas/`](aulas/) introduzem os assuntos de forma direta,
com explicações, código editável e resultados calculados durante a aula. Os
[notebooks](notebooks/) são o material suplementar para experimentar, resolver
exercícios e estudar com mais detalhes.

Para gerar e abrir as aulas no ambiente Pixi:

```sh
pixi install --locked
pixi run aulas-preview
```

Abra o endereço informado no terminal. O índice reúne as nove apresentações;
as setas navegam pelos slides. **Executar** avalia o código do editor e
**Restaurar código** recupera o exemplo original.

As apresentações foram construídas com [Quarto](https://quarto.org/) e
[Quarto Live](https://r-wasm.github.io/quarto-live/), usando Reveal.js e Pyodide.
O Pixi fornece as ferramentas de edição e geração; o código interativo das
apresentações roda em um Python separado, dentro do navegador. A preparação
inicial desse Python e das bibliotecas requer internet. As versões desse
ambiente são próprias do Pyodide, e não as do ambiente local do Pixi.

`pixi run aulas` gera o material em `aulas/_site/`. Essa pasta completa pode ser
servida com `pixi run aulas-servir`; abrir um HTML diretamente por `file://`
não oferece o servidor necessário aos arquivos usados pelos exemplos.
Veja [como editar e apresentar](aulas/README.md).

A extensão Quarto Live está incluída em `aulas/_extensions/r-wasm/live`,
fixada na tag `v0.2.0` (commit `d1459f7968efca5ccdb3cb8a993a399ec6d3e102`).
Sua licença MIT está preservada junto à extensão. O material autoral deste
curso usa CC BY 4.0.

## Comece por aqui

1. Instale o [Pixi](https://pixi.prefix.dev/latest/installation/), seguindo as instruções para seu sistema operacional. Feche e abra novamente o terminal e confira com `pixi --version`.
2. Obtenha esta pasta pelo material fornecido pelo professor ou por **Code → Download ZIP** no GitHub, e extraia o arquivo. O uso inicial não depende de conhecer Git.
3. Abra um terminal **dentro da pasta que contém `pixi.toml`**. No Windows, pode ser o PowerShell; no macOS ou Linux, o aplicativo de terminal. O comando `cd caminho/da/pasta` muda a pasta atual; use aspas se o caminho tiver espaços.
4. Prepare o ambiente e abra o JupyterLab:

   ```sh
   pixi install --locked
   pixi run lab
   ```

5. No navegador, abra `notebooks/00-ambiente-e-primeiro-notebook.ipynb`. Execute uma célula com **Shift+Enter**.

Na primeira instalação, o Pixi baixa o Python e as bibliotecas; é necessário acesso à internet. O terminal que abriu o Jupyter deve permanecer aberto. Para encerrar, volte a ele e pressione **Ctrl+C**, confirmando o encerramento se solicitado.

O ambiente inclui Python, NumPy, SciPy, Matplotlib e Jupyter. Para a interface Jupyter Notebook, use `pixi run notebook`. Para trabalhar no VS Code, abra esta pasta, instale as extensões Python e Jupyter e selecione o interpretador do ambiente Pixi como kernel do notebook. Veja os caminhos e a explicação de cada ferramenta no [guia do ambiente](docs/ambiente-pixi.md).

## Percurso dos cadernos

Os números indicam a ordem de leitura, **não uma correspondência de um caderno por encontro**. O conteúdo é retomado e distribuído pelas aulas da GA033.

| Caderno | O que vamos aprender | Quando usar |
| --- | --- | --- |
| [00 - Ambiente e primeiro notebook](notebooks/00-ambiente-e-primeiro-notebook.ipynb) | Pixi, células, kernel, execução e estado | Preparação e primeiro contato |
| [01 - Primeiros passos](notebooks/01-primeiros-passos.ipynb) | Tipos, operadores, listas, tuplas, dicionários e indexação | Fundamentos de Python |
| [02 - Controle de fluxo](notebooks/02-controle-de-fluxo.ipynb) | Condicionais, laços, `range`, `enumerate`, `zip` e comprehensions | Fundamentos de Python |
| [03 - Funções](notebooks/03-funcoes.ipynb) | Entradas, retorno, escopo, legibilidade e responsabilidades | Fundamentos; retomar durante implementação |
| [04 - Arrays com NumPy](notebooks/04-arrays-com-numpy.ipynb) | Dimensões, indexação, operações, cópias e sistemas lineares | Início das atividades numéricas |
| [05 - Gráficos e resultados](notebooks/05-graficos-e-resultados.ipynb) | Visualização, rótulos, comparação e interpretação de erros | Junto das primeiras aplicações |
| [06 - Cálculo científico com SciPy](notebooks/06-calculo-cientifico-com-scipy.ipynb) | Sistemas esparsos e integração numérica | Conforme a necessidade no MEF |
| [07 - Organização e dataclasses](notebooks/07-organizacao-e-dataclasses.ipynb) | Módulos, classes e representação de uma malha | Depois de trabalhar com funções e arrays |
| [08 - Tópicos complementares](notebooks/08-topicos-complementares.ipynb) | Raízes, ajuste de curvas, interpolação e EDOs | Consulta e aprofundamento opcional |

Boas práticas aparecem nos próprios exemplos: nomes com significado, funções com objetivo claro, separação entre cálculo e apresentação, verificação de resultados e cuidado com o estado do notebook. O [guia docente](docs/guia-docente.md) sugere como alternar explicações, programação ao vivo e pequenas atividades. O [guia de Git e GitHub](docs/git-e-github.md) entra antes da primeira entrega de código.

## O ambiente também faz parte da aula

O próprio repositório é o exemplo de projeto com Pixi:

- `pixi.toml` declara as dependências e os comandos do projeto.
- `pixi.lock` registra as dependências resolvidas para cada plataforma configurada.
- `.pixi/` contém o ambiente instalado localmente e fica fora do controle de versão.
- `src/malhalib/` contém o pequeno pacote Python com funções e uma classe de malha 1D.
- `pyproject.toml` descreve esse pacote. O Pixi instala `malhalib` em modo editável:
  mudanças no código de `src/` são utilizadas sem reinstalar o pacote.

Os primeiros passos usam o ambiente pronto. Mais adiante, o [guia de Pixi](docs/ambiente-pixi.md) explica como criar um pequeno projeto e reconhecer esses arquivos.

Para usar o pacote em código Python, importe seus módulos normalmente:

```python
from malhalib.malha import criar_malha_uniforme

malha = criar_malha_uniforme(4)
print(malha.comprimentos())
```

O pacote funciona a partir de outras pastas quando se usa o Python deste ambiente.
Em uma sessão que já importou o módulo, reinicie o kernel depois de editar sua fonte.

## Verificar e manter o material

Estes comandos destinam-se à manutenção do curso; os alunos podem começar diretamente pelos notebooks.

```sh
pixi run verificar
pixi run aulas-verificar
```

`verificar` confere o código de apoio, testa a representação de malha e executa
todos os notebooks em kernels novos, usando uma cópia temporária para preservar
os arquivos de trabalho. `aulas-verificar` executa os exemplos das apresentações
em namespaces independentes no Python local. Complete essa verificação com a
execução dos slides no navegador e com a revisão visual. Erros demonstrados
durante as aulas são capturados e explicados; a execução completa deve terminar
sem erros não tratados.

Para atualizar as saídas dos cadernos e exportá-los para leitura no navegador:

```sh
pixi run atualizar-saidas
pixi run html
```

Os arquivos HTML ficam em `resultados/html/`. Essa pasta contém resultados gerados e não é versionada. Veja [como contribuir](CONTRIBUTING.md) e o [registro da revisão](docs/origem-e-revisao.md).

## Autoria, licença e citação

O material autoral deste módulo é disponibilizado sob a licença **Creative Commons Atribuição 4.0 Internacional (CC BY 4.0)**. É permitido compartilhar e adaptar o material, com atribuição a **Diego Tavares Volpatto**, indicação da licença e das alterações realizadas. Consulte a [licença](LICENSE) e o [resumo em português](https://creativecommons.org/licenses/by/4.0/deed.pt-br).

Uma forma de citar:

> VOLPATTO, Diego Tavares. *Introdução à programação científica com Python: módulo da disciplina GA033 - Método de Elementos Finitos: Implementação Computacional*. LNCC, 2026. Disponível em: https://github.com/lncc-ga033/intro-to-scientific-python-programming. Licença CC BY 4.0.

Os dados de citação também estão em [CITATION.cff](CITATION.cff). Materiais de terceiros eventualmente referenciados ou presentes nas ilustrações conservam suas próprias atribuições e condições de uso.

## Referências

- [Curso de NumPy e SciPy de Diego Volpatto (2019)](https://github.com/volpatto/numpy_scipy_course)
- [Tutorial de Python em português](https://docs.python.org/pt-br/3/tutorial/)
- [Documentação do NumPy](https://numpy.org/doc/stable/)
- [Documentação do SciPy](https://docs.scipy.org/doc/scipy/)
- [Documentação do Matplotlib](https://matplotlib.org/stable/)
- [Documentação do Pixi](https://pixi.prefix.dev/latest/)
- [Pro Git em português](https://git-scm.com/book/pt-br/v2)
