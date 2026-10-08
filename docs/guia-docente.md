# Guia docente -- fundamentos computacionais da GA033

Este material é um módulo de apoio à GA033 para estudantes sem experiência ou sem hábito de programar em Python. O objetivo é permitir que leiam, modifiquem, verifiquem e, progressivamente, organizem os códigos usados no curso de elementos finitos.

Os cadernos são uma sequência de estudo e consulta. Não precisam ser apresentados integralmente em uma única aula. Completar sua execução também não demonstra, por si só, que o estudante compreendeu cada operação.

## Preparação e ambiente

Antes da primeira prática, conferir o procedimento de [preparação com Pixi](ambiente-pixi.md) nas máquinas que serão usadas. A instalação deve ser testada com antecedência, inclusive abertura do Jupyter e execução de uma célula. Não presumir que todos saibam localizar uma pasta ou abrir um terminal.

Na aula, começar com o comando mínimo necessário para trabalhar: `pixi run lab` ou `pixi run notebook`. O ambiente preparado já constitui um exemplo de organização reprodutível. Explicar manifesto, arquivo de bloqueio e tarefas quando os alunos tiverem executado um cálculo e puderem reconhecer o problema que essas ferramentas resolvem.

Os comandos `pixi run testar` e `pixi run verificar` fazem parte da manutenção do material. Apresentá-los depois que houver verificações concretas para discutir. Um comando que termina sem erro não substitui a interpretação das saídas e dos resultados científicos.

## Distribuição ao longo da GA033

| Momento | Conteúdo de programação | Ligação com o trabalho científico |
|---|---|---|
| Primeiro contato | Caderno 00 e início do 01: células, nomes, tipos, operações, comparações e listas. | Alterar dados e prever como muda uma conta curta. |
| Fundamentos, com retomadas nas aulas seguintes | Restante do 01 e caderno 02: coleções, cópias, indexação, condicionais, laços e comprehensions. | Percorrer medições, identificar extremos, acumular valores e controlar uma repetição. |
| Primeiros cálculos organizados | Caderno 03: entradas, retorno, argumentos, escopo, documentação e verificações. | Separar uma expressão matemática de sua apresentação; conferir casos conhecidos. |
| Primeira implementação de Poisson 1D | Cadernos 04 e 05, retomando laços e funções. | Representar nós e matrizes, verificar dimensões e comparar valores calculados com uma referência. |
| Depois de um primeiro programa funcional | Introdução de módulos e fluxo mínimo de Git. | Reutilizar funções entre experimentos e registrar uma alteração que já foi verificada. |
| Cálculos que exigem ferramentas adicionais | Caderno 06, conforme a necessidade. | Escolher quadratura, álgebra linear ou outra rotina a partir do problema; conferir suas hipóteses e saídas. |
| Crescimento do código e dos dados | Caderno 07: organização, classes e dataclasses, após funções e módulos. | Agrupar informações que circulam juntas e explicitar condições de consistência. |
| Aprofundamento | Caderno 08 e retomadas pontuais. | Tratar novas necessidades sem interromper a primeira experiência com uma apresentação extensa de recursos da linguagem. |

Essa ordem não exige concluir todo o Python antes de falar de elementos finitos. Exige distinguir o que o aluno já consegue usar sozinho do que está apenas acompanhando em um exemplo guiado. Quando um conceito novo aparecer no código do método, reservar tempo para explicá-lo e exercitá-lo.

## Um início possível em dois encontros de 90 minutos

Três horas permitem começar, não dominar Python, NumPy, SciPy, Pixi e Git. Para iniciantes reais, os cadernos 01–03 demandam tempo adicional de prática e retomada.

No primeiro encontro, priorizar execução de células, variáveis, operações, tipos básicos, f-strings, listas e indexação. Usar o caderno 01 de forma seletiva e reservar parte do tempo para os alunos alterarem os dados e resolverem pelo menos um exercício. Se a instalação consumir a aula, reduzir o conteúdo previsto e marcar uma retomada; não compensar acelerando a exposição.

No segundo encontro, retomar listas e apresentar `if`, `for`, `range` e acumulação. Fazer uma pequena atividade em que os estudantes tenham de prever e depois modificar um laço. Introduzir uma função com entradas e retorno a partir de um cálculo que a turma já realizou. É razoável terminar esse encontro com uma função curta funcionando, mesmo que os demais recursos ainda não tenham sido vistos.

Tuplas, dicionários, conjuntos, mutabilidade, `while`, `enumerate`, `zip`, `break`, `continue` e comprehensions continuam tendo tratamento explícito nos cadernos e nas aulas seguintes. Comprehensions devem vir depois do laço equivalente. Não transformar a revisão em uma lista de nomes de recursos sem prática.

Ao planejar atividades fora da aula, indicar um trecho curto, um resultado esperado e uma forma de pedir ajuda. A leitura autônoma não substitui a retomada dos conceitos que a turma ainda não assimilou.

## Alternar ilustração, código e participação

Um ciclo de trabalho pode começar com um desenho curto no Excalidraw, seguir para uma célula de código e terminar com uma alteração feita pelos estudantes. A duração deve acompanhar a resposta da turma.

1. **Mostrar a relação.** Desenhar, por exemplo, uma sequência com seus índices, uma decisão com duas saídas ou uma função com entradas e retorno.
2. **Pedir uma previsão.** Antes de executar, perguntar quais linhas serão percorridas e qual resultado se espera.
3. **Executar e conferir.** Escrever poucas linhas, observar a saída e relacioná-la ao desenho.
4. **Alterar um dado ou uma regra.** Mudar um limite, uma lista ou uma expressão. Dar tempo para que os alunos executem e expliquem a mudança.
5. **Retomar a ideia.** Pedir que alguém descreva o que o código faz, sem apenas ler sua sintaxe.

Desenhos úteis para os primeiros cadernos:

- Uma lista com índices positivos e negativos; a faixa selecionada por uma fatia.
- Dois nomes apontando para a mesma lista e uma terceira referência apontando para uma cópia.
- Um `if`/`elif`/`else` com os limites das faixas escritos nas setas.
- Um laço com “ler item → calcular → atualizar acumulador”, mostrando a mudança de estado.
- Uma função como “entradas → cálculo → resultado”, separada da impressão.

Evitar desenhar de início uma arquitetura completa de software. O desenho deve explicar a operação que está sendo programada naquele momento.

## Diluir legibilidade e organização

Desde o primeiro caderno, usar nomes que expressem o papel de cada dado. `indice` e `posicao` não são sinônimos; `numero_elementos` e `numero_nos` também não. Nomes matemáticos usuais, como `x`, `A` e `b`, podem ser adequados quando sua correspondência com as equações estiver explícita.

Introduzir funções quando houver um cálculo que vale a pena nomear, reutilizar ou verificar separadamente. Nas primeiras implementações de MEF, podem surgir funções para avaliar uma fonte, calcular uma contribuição local, montar os termos globais, impor contornos e apresentar resultados. Não é necessário criar todas essas funções antes de a turma compreender cada etapa.

Organizar em módulos quando começar a haver reutilização entre cadernos ou experimentos. Um módulo de funções de cálculo e um notebook de experimentos podem ser suficientes no início. Não criar um arquivo por função apenas para aumentar a estrutura do projeto.

Apresentar classes e dataclasses **depois de funções e módulos**. Uma dataclass pode ser útil quando dados de uma malha, como nós e conectividade, são passados juntos repetidamente. Ela organiza os campos, mas não garante automaticamente dimensões, unidades, conectividade válida nem imutabilidade dos objetos guardados. Essas condições precisam ser discutidas e, quando apropriado, verificadas.

Métodos devem aparecer quando houver operações que se beneficiem dessa organização. Uma classe que apenas envolve todas as funções em um único objeto não é, por isso, um código mais claro.

## Git e reprodução dos resultados

Introduzir o fluxo mínimo de [Git e GitHub](git-e-github.md) depois dos primeiros programas funcionais e antes da primeira entrega de projeto. Começar por ver alterações, registrar uma versão e enviar o trabalho. Deixar branches e resolução de conflitos para quando houver uma situação que justifique esses assuntos.

Mostrar que a execução depende do código e dos dados usados. Para notebooks, reforçar a execução em um núcleo novo. Uma célula pode funcionar por causa de um nome criado anteriormente e já removido do texto; reiniciar e executar tudo ajuda a identificar essa dependência oculta.

## Observações para os cadernos 01–03

- As células de exercícios têm valores provisórios e executam sem interrupção. Elas não devem ser usadas como respostas corretas. Pedir a comparação com os resultados esperados no enunciado.
- Nas demonstrações, as entradas numéricas são valores finitos e compatíveis com o cálculo. Isso não significa que todas as funções de exemplo validem qualquer tipo ou valor que um usuário possa fornecer.
- `ValueError` é usado para explicar uma entrada rejeitada. O erro intencional está capturado; não desativar a execução completa para acomodar erros esperados.
- `math.isclose` é apresentado com tolerâncias explícitas para exemplos escalares. As tolerâncias precisam ser escolhidas conforme a escala e a finalidade de cada verificação.
- Comparar valores em uma lista de pontos não fornece automaticamente o erro máximo de uma função em todo o domínio.
- A fonte e a função de referência do caderno 03 são apenas expressões para avaliar. O caderno não ensina um solver nem antecipa a resolução de uma atividade avaliativa de MEF.

## Soluções comentadas dos exercícios

As soluções abaixo são uma possibilidade. Em aula, conferir primeiro a interpretação do enunciado e as escolhas dos alunos. Os blocos são independentes: podem ser executados separadamente. A numeração se refere aos exercícios dos cadernos, não a listas de avaliação da disciplina.

### Caderno 01, exercício 1 -- Variação

```python
temperatura_inicial = 18.5
temperatura_final = 24.0
variacao_temperatura = temperatura_final - temperatura_inicial
mensagem = f"Variação de temperatura: {variacao_temperatura:.1f} °C."
print(mensagem)
```

O resultado é `5.5` °C. Inverter as duas temperaturas produz `-5.5` °C. A f-string apresenta o resultado; ela não faz parte da definição matemática da variação.

### Caderno 01, exercício 2 -- Consulta e cópia

```python
temperaturas = [20.0, 21.5, 22.0, 23.0, 23.5]
medicao_central = temperaturas[2]
tres_primeiras = temperaturas[:3]
temperaturas_corrigidas = temperaturas.copy()
temperaturas_corrigidas[-1] = 24.0

print(medicao_central)
print(tres_primeiras)
print(temperaturas)
print(temperaturas_corrigidas)
```

A medição central é `22.0`, e a fatia contém `[20.0, 21.5, 22.0]`. A última medição da lista original permanece `23.5`. Trocar `copy()` por uma atribuição direta faria os dois nomes acessarem a mesma lista.

### Caderno 01, exercício 3 -- Configuração

```python
experimento = {
    "nome": "medição de temperatura",
    "repeticoes": 3,
    "ativo": True,
}
nova_configuracao = experimento.copy()
nova_configuracao["repeticoes"] = 5
descricao = (
    f"{nova_configuracao['nome']}: "
    f"{nova_configuracao['repeticoes']} repetições."
)
print(experimento)
print(nova_configuracao)
print(descricao)
```

São dois dicionários distintos. Para os valores imutáveis deste exemplo, a cópia superficial é suficiente. Não generalizar essa independência a dicionários que contenham listas ou outros objetos mutáveis.

### Caderno 02, exercício 1 -- Extremos e interior

```python
posicoes = [0.0, 0.25, 0.50, 0.75, 1.0]
ultimo_indice = len(posicoes) - 1

for indice, posicao in enumerate(posicoes):
    if indice == 0 or indice == ultimo_indice:
        classificacao = "extremo"
    else:
        classificacao = "interior"
    print(f"Nó {indice}, posição {posicao:.2f}: {classificacao}")
```

Os nós `0` e `4` são extremos. A condição utiliza a posição na sequência, não uma comparação aproximada das coordenadas. O exemplo pressupõe uma sequência ordenada dos nós ao longo de um intervalo.

### Caderno 02, exercício 2 -- Busca com tolerância

```python
valores = [0.10, 0.30, 0.48, 0.51, 0.80]
alvo = 0.50
tolerancia = 0.03
valor_encontrado = None

for valor in valores:
    if abs(valor - alvo) <= tolerancia:
        valor_encontrado = valor
        break

print(valor_encontrado)
```

O resultado é `0.48`. Sem `break`, uma busca que continua sobrescrevendo o resultado pode terminar com outro valor. Isso mostra por que “primeiro valor admissível” e “valor mais próximo” são problemas diferentes.

### Caderno 02, exercício 3 -- Comprehensions

```python
temperaturas_celsius = [-5.0, 0.0, 20.0, 35.0]
temperaturas_kelvin = [
    temperatura + 273.15 for temperatura in temperaturas_celsius
]
temperaturas_positivas = [
    temperatura for temperatura in temperaturas_celsius if temperatura > 0.0
]

kelvin_com_laco = []
for temperatura in temperaturas_celsius:
    kelvin_com_laco.append(temperatura + 273.15)

print(temperaturas_kelvin)
print(temperaturas_positivas)
print(temperaturas_kelvin == kelvin_com_laco)
```

As duas construções em kelvin realizam as mesmas operações na mesma ordem. A igualdade entre essas listas não constitui uma regra geral para comparar resultados obtidos por algoritmos numéricos diferentes.

### Caderno 03, exercício 1 -- Retorno

```python
import math


def atualizar_temperatura(temperatura, variacao):
    """Retorna a temperatura após somar a variação informada."""
    return temperatura + variacao


assert math.isclose(atualizar_temperatura(20.0, 3.0), 23.0, abs_tol=1e-12)
assert math.isclose(atualizar_temperatura(20.0, -2.0), 18.0, abs_tol=1e-12)
print(atualizar_temperatura(20.0, 3.0))
print(atualizar_temperatura(20.0, -2.0))
```

A função devolve o resultado para que ele possa ser usado em outro cálculo. A impressão continua no código que a chama.

### Caderno 03, exercício 2 -- Fluxo e validação

```python
import math


def calcular_fluxo(condutividade, gradiente):
    """Retorna -k * gradiente para escalares finitos, com k positivo."""
    if condutividade <= 0.0:
        raise ValueError("A condutividade deve ser positiva.")
    return -condutividade * gradiente


fluxo = calcular_fluxo(2.0, -3.0)
assert math.isclose(fluxo, 6.0, rel_tol=1e-12, abs_tol=1e-12)
print(fluxo)

try:
    calcular_fluxo(0.0, -3.0)
except ValueError as erro:
    print(f"Erro esperado: {erro}")
```

O sinal é parte do modelo: para condutividade positiva, o fluxo tem sentido oposto ao gradiente. A validação implementada verifica positividade; neste exercício, os argumentos são escalares reais finitos. Um tratamento geral de dados externos pode exigir outras verificações.

### Caderno 03, exercício 3 -- Média e entrada vazia

```python
import math


def calcular_media(valores):
    """Retorna a média aritmética de uma sequência não vazia."""
    if len(valores) == 0:
        raise ValueError("A sequência de valores não pode estar vazia.")
    return sum(valores) / len(valores)


assert math.isclose(
    calcular_media([2.0, 4.0, 6.0]), 4.0, rel_tol=1e-12, abs_tol=1e-12
)
assert math.isclose(
    calcular_media([5.0]), 5.0, rel_tol=1e-12, abs_tol=1e-12
)
print(calcular_media([2.0, 4.0, 6.0]))

try:
    calcular_media([])
except ValueError as erro:
    print(f"Erro esperado: {erro}")
```

A média de uma sequência vazia não é definida por essa fórmula. Uma mensagem explícita é mais informativa que deixar a execução chegar a uma divisão por zero.

## Critérios de acompanhamento

Pedir que o estudante explique uma célula, altere um dado e confira o resultado. Antes de avançar, observar se ele distingue índice de valor, atribuição de comparação e retorno de impressão.

Quando aparecer um erro, localizar a entrada, a operação e a hipótese envolvida. Evitar corrigir apenas a linha apontada pela mensagem sem compreender a causa. Para um cálculo científico, distinguir erro de programação, escolha do modelo e limitação numérica.

Autoria: Diego Tavares Volpatto. Material didático da GA033 distribuído sob a licença indicada em [LICENSE](../LICENSE), CC BY 4.0.
