# Um ambiente para acompanhar a GA033

O projeto reúne o código e a descrição dos programas necessários para executá-lo. O Pixi prepara esse ambiente para que a turma trabalhe com um conjunto conhecido de dependências.

## Quem faz o quê?

| Componente | Papel nesta aula |
| --- | --- |
| Python | Linguagem em que escrevemos os cálculos; o interpretador executa o código. |
| NumPy, SciPy e Matplotlib | Bibliotecas que fornecem arrays, métodos numéricos e gráficos. |
| JupyterLab ou Jupyter Notebook | Interface no navegador para alternar texto, código e resultados. |
| Kernel | Processo Python que executa as células e mantém as variáveis em memória. |
| Pixi | Gerencia as dependências do projeto e executa comandos dentro do ambiente. |
| Git | Registra versões dos arquivos do projeto. |

O navegador exibe o notebook; o código é executado pelo kernel. Fechar uma aba não equivale a reiniciar o Python nem a encerrar o servidor Jupyter.

## 1. Preparar o ambiente fornecido

Instale o Pixi seguindo a [documentação oficial](https://pixi.prefix.dev/latest/installation/), na seção do seu sistema operacional. Abra um novo terminal e confira:

```sh
pixi --version
```

Obtenha e extraia a pasta do curso. Abra o terminal nessa pasta, onde estão `README.md` e `pixi.toml`. Por exemplo, substituindo o caminho pelo local em que você salvou a pasta:

```sh
cd "caminho/para/intro-to-scientific-python-programming"
pixi install --locked
pixi run lab
```

O primeiro comando do Pixi instala o ambiente usando o arquivo de versões do curso. A opção `--locked` impede que o arquivo de versões seja atualizado silenciosamente caso ele esteja incompatível com a declaração de dependências.

O segundo inicia o JupyterLab. Abra `notebooks/00-ambiente-e-primeiro-notebook.ipynb` na lista de arquivos e escolha o kernel Python 3 do ambiente. Caso o navegador não abra automaticamente, use o endereço local exibido no terminal. Mantenha esse terminal aberto durante a atividade.

Para a interface Jupyter Notebook, há outra tarefa preparada:

```sh
pixi run notebook
```

Escolha uma interface e use-a durante a aula. Ambas executam os mesmos arquivos `.ipynb`.

## 2. Reconhecer os arquivos do ambiente

Abra `pixi.toml` e localize três seções:

- `[workspace]`: identifica o projeto, seus canais e plataformas.
- `[dependencies]`: declara Python e bibliotecas, com intervalos de versões aceitos.
- `[tasks]`: dá nomes aos comandos que repetimos durante o trabalho.

Por exemplo, a tarefa `lab = "jupyter lab"` permite usar `pixi run lab`. O Pixi executa esse comando dentro do ambiente do projeto.

O `pixi.lock` registra os pacotes resolvidos e suas versões por plataforma. Esse arquivo é gerado pelo Pixi; acompanha o projeto e normalmente não é editado manualmente. Já a pasta `.pixi/` é criada localmente e pode ser reconstruída a partir da descrição do ambiente. Por isso ela está no `.gitignore`.

**Ambiente reproduzível não significa máquina idêntica.** O ambiente descreve dependências de software. Hardware, sistema operacional, bibliotecas numéricas e ordem das operações também podem influenciar resultados em ponto flutuante. A verificação de resultados científicos usa tolerâncias apropriadas ao problema.

## 3. Criar um projeto pequeno durante a aula

Faça esta atividade em uma pasta nova, fora da pasta do curso. Assim fica fácil observar quais arquivos cada comando cria.

```sh
pixi init meu-primeiro-calculo
cd meu-primeiro-calculo
pixi add python numpy matplotlib
pixi run python
```

O último comando abre o interpretador. Quando aparecer `>>>`, escreva **código Python**, por exemplo:

```python
import numpy as np
coordenadas = np.linspace(0.0, 1.0, 5)
print(coordenadas)
exit()
```

De volta ao terminal, compare os arquivos da pasta com os do curso. Quais dependências foram declaradas? Onde as versões resolvidas foram registradas? O novo projeto usa as versões resolvidas naquele momento; não é uma cópia automática do ambiente do curso.

## 4. Se preferir usar o VS Code

Abra a pasta inteira do curso no VS Code. Instale as extensões Python e Jupyter. Depois, abra um notebook e escolha **Select Kernel → Python Environments**, selecionando o interpretador deste projeto:

- macOS/Linux: `.pixi/envs/default/bin/python`;
- Windows: `.pixi/envs/default/python.exe`.

Se ele não aparecer automaticamente, selecione o caminho do interpretador. O nome visual do kernel pode variar entre versões do editor. O importante é que o notebook use o Python do ambiente Pixi deste projeto.

## Dificuldades frequentes

| Situação | O que conferir |
| --- | --- |
| O terminal não reconhece `pixi` | Reabra o terminal após instalar; confira a instalação e a configuração do PATH indicada na documentação. |
| O Pixi não encontra o manifesto | Você está na pasta que contém `pixi.toml`? |
| `import numpy` falha no notebook | Confira o kernel selecionado. Abrir o Jupyter com `pixi run lab` ajuda a usar o ambiente correto. |
| Uma variável funciona em uma sessão e falha em outra | Reinicie o kernel e execute as células de cima para baixo. |
| A instalação com `--locked` acusa divergência | Confira se `pixi.toml` e `pixi.lock` vieram da mesma versão do material. Ao manter o curso, atualize ambos de forma intencional. |

## Ilustração para a aula

O [painel original de Pixi](figuras/pixi.png) e sua [fonte editável](figuras/pixi.excalidraw) estão preservados. Use primeiro a motivação e os ambientes por projeto; a comparação com contêineres pode ser retomada depois. Ao comentar o painel, substitua a ideia de “máquinas idênticas” pela distinção entre dependências reproduzíveis e características da máquina. Contêineres isolam processos e compartilham o kernel do sistema em que executam; não são máquinas virtuais completas.

Referências: [primeiro projeto com Pixi](https://pixi.prefix.dev/latest/first_workspace/), [contêineres na documentação do Docker](https://docs.docker.com/get-started/docker-concepts/the-basics/what-is-a-container/).
