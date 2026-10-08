# Git e GitHub: um primeiro ciclo de trabalho

Este roteiro acompanha o módulo introdutório de programação científica da GA033.
O objetivo é reconhecer o que mudou, registrar uma versão e, quando apropriado,
compartilhá-la. Git cuida do histórico; GitHub hospeda repositórios e oferece
recursos de colaboração.

Os comandos abaixo são exemplos para a atividade. Antes da aula, tenha Git e
Pixi instalados e use uma pasta de trabalho que você consiga localizar. Execute
um bloco por vez e confira o resultado antes de continuar.

## 1. Abrir uma cópia do material

Quando o repositório do curso estiver publicado, este será o endereço para cloná-lo:

```console
git clone https://github.com/lncc-ga033/intro-to-scientific-python-programming.git
cd intro-to-scientific-python-programming
git status
```

Um clone é um repositório local com o histórico disponível no remoto, além dos
arquivos de trabalho. É possível editar e registrar commits sem conexão com a
internet. O repositório compartilhado é a referência escolhida pela equipe;
Git não depende de um computador central para registrar versões locais.

Para executar os exemplos, siga as tarefas Pixi descritas no README do projeto.
O arquivo `pixi.toml` declara dependências e tarefas; `pixi.lock` registra as
dependências resolvidas. Esses dois arquivos fazem parte do material versionado.

## 2. Salvar, selecionar e registrar são ações diferentes

| Ação | O que acontece |
|---|---|
| Salvar no editor | O arquivo de trabalho muda no seu computador. |
| Selecionar para o próximo commit (*stage*) | Você escolhe quais mudanças entrarão no registro. |
| Fazer um commit | Git registra localmente o estado selecionado, com uma mensagem. |
| Fazer um push | Os commits são enviados para um repositório remoto, se houver permissão. |

Use primeiro um arquivo de texto pequeno, para enxergar facilmente a diferença.
No repositório de exercício, crie ou edite `anotacoes.md`, escreva uma frase sobre
o que aprendeu e salve. Em seguida:

```console
git status
git diff
git add anotacoes.md
git diff --staged
git commit -m "Registra primeira observacao sobre o exemplo"
git log --oneline -3
```

`git diff` mostra mudanças ainda não selecionadas. `git diff --staged` mostra o
que será registrado. A saída do commit confirma um registro **local**: o GitHub
ainda não recebeu essa mudança. Se Git solicitar nome e e-mail, configure sua
identidade conforme a orientação da aula antes de repetir o commit.

Se você editar o arquivo novamente depois de `git add`, a nova edição ainda não
estará selecionada. Observe isso em `git status`. Essa experiência costuma
explicar melhor a seleção do que decorar comandos.

## 3. O que entra no histórico?

Versionamos o código, os notebooks, os textos e os arquivos que descrevem o
ambiente. A pasta do ambiente instalado não deve ser enviada. Um exemplo de
entrada no arquivo `.gitignore` é:

```gitignore
.pixi/
```

O projeto já fornece seu `.gitignore`; não é preciso substituí-lo por esse
trecho. **`pixi.toml` e `pixi.lock` devem continuar versionados.** O ambiente
`.pixi/` é reconstruído a partir deles. Evite selecionar indiscriminadamente
arquivos grandes de resultados, cópias temporárias ou credenciais.

## 4. Compartilhar no repositório do exercício

Clonar o material do curso não concede permissão para alterá-lo no GitHub.
Para esta etapa, use o repositório atribuído à sua atividade, ou outro
repositório em que você tenha permissão de gravação. A autenticação deve estar
pronta antes da execução ao vivo.

Neste exemplo, usamos uma branch para a atividade. Esse fluxo ajuda a separar
propostas; não é uma exigência para todo uso de Git. Siga o fluxo indicado pelo
professor para cada atividade do curso.

```console
git switch -c atividade-anotacao
git status
```

Edite, salve, selecione e faça um commit como na etapa anterior. Depois:

```console
git push -u origin atividade-anotacao
```

Esse comando publica a branch de trabalho. Ele não faz sua branch entrar
automaticamente em `main`. No GitHub, abra um **pull request** para propor a
integração, confira as alterações e peça a revisão prevista na atividade.
Abrir o PR propõe; fazer o **merge** integra. A analogia com submissão e revisão
de um artigo ajuda a distinguir as duas etapas.

Depois que a proposta for integrada, e com o trabalho local salvo e registrado,
é possível atualizar a branch principal:

```console
git switch main
git pull --ff-only
```

Usamos `--ff-only` para que esse primeiro fluxo pare se os históricos tiverem
divergido, em vez de criar uma integração inesperada. Se isso acontecer, leia a
mensagem com o professor. Não use comandos para descartar mudanças apenas para
fazer a mensagem desaparecer.

## 5. Alternar o desenho com uma ação observável

Os diagramas fornecidos pelo professor permanecem como referências originais:

- [Painel Git, editável no Excalidraw](figuras/git.excalidraw) e [imagem Git](figuras/git.png).
- [Painel Pixi, editável no Excalidraw](figuras/pixi.excalidraw) e [imagem Pixi](figuras/pixi.png).

Uma sequência curta para a aula:

1. Mostre as várias cópias de um arquivo; compare duas versões com `git diff`.
2. Mostre a linha de commits; faça um commit e veja `git log`.
3. Mostre local e remoto; publique a branch do exercício e confira no GitHub.
4. Mostre a proposta de integração; abra um PR e identifique a etapa de revisão.
5. Mostre o ambiente do projeto; execute um exemplo pelo Pixi e altere um dado.

Os desenhos de múltiplas branches, hot-fix, conflitos e rebase ficam como
continuação. Nesta primeira passagem, priorize completar e compreender um ciclo.
Git ajuda a localizar e integrar mudanças, mas não impede conflitos nem verifica
se um resultado científico está correto.

No painel de ambientes, interprete “reproduzir” como reconstruir as dependências
registradas para a plataforma escolhida. Pixi não copia todo o sistema
operacional nem garante resultados numéricos idênticos entre quaisquer máquinas.
Contêineres são outro mecanismo: isolam processos e compartilham o kernel do
ambiente que os executa; não precisam ser estudados nesta primeira prática.

## Para conferir sozinho

- Consigo dizer quais mudanças estão somente salvas e quais estão selecionadas?
- Meu commit aparece no histórico local? Ele já foi publicado?
- O PR está aberto ou já foi integrado?
- O código foi executado no ambiente Pixi descrito pelo projeto?

Referências: [registro de mudanças no Git](https://git-scm.com/book/en/v2/Git-Basics-Recording-Changes-to-the-Repository),
[pull requests no GitHub](https://docs.github.com/en/pull-requests/get-started/about-pull-requests)
e [manifesto do Pixi](https://pixi.prefix.dev/latest/reference/pixi_manifest/).

Autor: Diego Tavares Volpatto. Licença: [CC BY 4.0](https://creativecommons.org/licenses/by/4.0/).
