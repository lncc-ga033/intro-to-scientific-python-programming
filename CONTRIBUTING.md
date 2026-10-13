# Revisão e manutenção

Este material é um módulo da GA033/LNCC, escrito em português brasileiro para estudantes iniciantes em Python. Preserve as explicações progressivas e a relação entre cada exemplo e seu objetivo de aprendizagem.

## Preparar o trabalho

```sh
pixi install --locked
pixi run lab
```

Edite os arquivos `.ipynb` diretamente no Jupyter. Eles são a fonte dos cadernos. Use o ambiente do repositório e reinicie o kernel antes da execução final. Textos, instruções e comentários devem estar em PT-BR; nomes da API de Python e de bibliotecas permanecem como definidos por elas.

As fontes das apresentações são os arquivos `.qmd` em `aulas/`. Use a identidade
visual comum e confira o resultado no navegador. Cada slide deve explicar um
conceito e manter seu exemplo curto e independente. Os notebooks complementam
as aulas com estudo e exercícios. Veja o [guia das apresentações](aulas/README.md).

O código de apoio está em `src/malhalib/`, instalado em modo editável pelo Pixi.
Edite os módulos nessa pasta e importe-os como `malhalib`. Não é necessário
acrescentar caminhos a `sys.path`. Reinicie os kernels que já importaram o módulo
para que utilizem as alterações.

## Critérios para exemplos

- Explique os pré-requisitos e mantenha pequenas as células de código.
- Introduza laços antes de comprehensions e funções antes de classes.
- Use dados determinísticos ou um gerador aleatório com semente explícita.
- Compare resultados numéricos com tolerâncias justificáveis; separe resíduo algébrico de erro da aproximação.
- Identifique resultados medidos como medições, sem extrapolar um ganho de tempo para uma mudança de complexidade.
- Capture erros intencionais para que o notebook possa ser executado inteiro.
- Deixe soluções de exercícios claramente identificadas, no guia ou em trechos recolhíveis.
- Inclua atribuição ao reaproveitar material e respeite as licenças das fontes.

## Validar uma alteração

```sh
pixi run verificar
pixi run atualizar-saidas
pixi run html
pixi run aulas-verificar
pixi run aulas
```

Além da execução, confira os gráficos e leia a sequência completa no Jupyter ou nos arquivos de `resultados/html/`: rótulos, legendas, unidades, fórmulas, resultados esperados e dependências entre células. Testes dos módulos não substituem a revisão matemática e didática.

`pixi.toml` e `pixi.lock` devem acompanhar as mudanças de dependências. A resolução para várias plataformas não comprova execução em todas elas; registre em qual sistema a validação foi realizada.
