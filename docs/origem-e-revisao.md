# Origem e critérios da revisão

Este crash course é um módulo da GA033 -- Método de Elementos Finitos: Implementação Computacional, do LNCC. Autor: Diego Tavares Volpatto. Material autoral sob CC BY 4.0.

## Material consultado

- Curso [NumPy/SciPy de 2019](https://github.com/volpatto/numpy_scipy_course), revisão consultada `9939089d7a2e28593403d7fbeec6a1791ae287f0`.
- Diagramas de Git e Pixi fornecidos pelo professor, preservados em `docs/figuras/` com suas fontes Excalidraw.
- Documentação oficial das bibliotecas, indicada ao final dos cadernos.

O curso de 2019 integrava uma formação cuja introdução a Python foi ministrada por Pedro Siracusa. Os dois notebooks disponibilizados por Diego tratavam de NumPy e SciPy. Este módulo acrescenta os fundamentos de Python para uma turma que ainda não domina a linguagem.

Os cadernos desta revisão foram redigidos para o novo percurso, com exemplos pequenos e determinísticos. O repositório de 2019 permanece uma referência histórica; sua licença e as licenças das fontes que ele cita não são alteradas por esta revisão.

## O que foi reaproveitado e reorganizado

| Ideia presente no material anterior | Tratamento neste módulo |
| --- | --- |
| Arrays, formas, indexação e operações | Caderno 04, depois de listas, laços e funções. |
| Cópias e visões | Exemplos que distinguem alteração dos dados de atribuição de um novo objeto. |
| Álgebra linear densa e esparsa | Sistemas pequenos, solução direta e conferência do resíduo nos cadernos 04 e 06. |
| Gráficos | Unidade própria, com rótulos, legendas e interpretação. |
| Quadratura | Estimativa do erro e comparação com integral conhecida. |
| Raízes, ajustes, interpolação e EDOs | Complemento opcional no caderno 08. |
| Preparação do ambiente | Pixi, com manifesto, arquivo de versões e tarefas usados pela própria aula. |

## Correções conceituais adotadas

- Ganho de tempo de uma operação vetorizada não é, por si só, mudança de sua complexidade assintótica.
- O produto `outer` de vetores e o produto de Kronecker de matrizes têm definições diferentes; não são apresentados como intercambiáveis.
- A solução de um sistema linear é feita por um solucionador, sem formar a inversa da matriz como procedimento padrão.
- Resíduo algébrico pequeno não comprova, sozinho, erro pequeno na solução de um problema mal condicionado ou na aproximação de uma EDP.
- Erros de quadratura retornados pela biblioteca são estimativas, não conhecimento do erro exato.
- Algoritmos de raízes e otimização são apresentados com suas condições e critérios; não há ranking universal de “melhor método”.
- Dataclasses organizam dados e geram métodos auxiliares; a validação dos dados precisa ser programada.

## Ilustrações fornecidas

As imagens e fontes de Git/Pixi foram preservadas para aproveitar a apresentação do professor. Os guias explicam as distinções a adotar durante a exposição, incluindo commit versus publicação, proposta de pull request versus integração e ambiente versus máquina. As imagens originais ainda contêm as formulações anteriores: devem ser usadas em trechos, acompanhadas dessas correções, até uma revisão gráfica específica.

Créditos e condições de uso de elementos de terceiros presentes nas ilustrações permanecem aplicáveis; a licença do curso se refere ao material autoral.

## Como verificar a revisão

`pixi run verificar` executa os notebooks em kernels novos e testa o módulo de malha. A tarefa não compara a apresentação visual automaticamente. Para conferir a diagramação dos gráficos e a sequência didática, use o Jupyter ou `pixi run html`.

O manifesto contempla macOS (Apple Silicon e Intel), Linux x86-64 e Windows x86-64. A resolução de dependências para essas plataformas não equivale à execução do curso em cada sistema; a validação local deve ser registrada separadamente.
