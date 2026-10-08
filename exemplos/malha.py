"""Uma estrutura simples para coordenadas e elementos de uma malha 1D.

O exemplo ensina organização de dados e validação. Não resolve uma equação
diferencial nem verifica se os elementos cobrem um domínio sem lacunas.
"""

from dataclasses import dataclass
from numbers import Real

import numpy as np

from .calculos import calcular_comprimentos


@dataclass(eq=False)
class Malha1D:
    """Guarda coordenadas reais e pares de índices dos nós dos elementos.

    A construção copia os arrays e verifica sua estrutura. Cada elemento deve
    apontar do nó de menor coordenada para o de maior coordenada. Os atributos
    continuam mutáveis: esta classe não promete imutabilidade nem revalida
    alterações feitas depois da construção.

    ``eq=False`` evita a comparação automática de arrays pelo ``==`` gerado
    por dataclass. Para comparar dados, use ``np.array_equal`` ou
    ``np.allclose``, conforme a finalidade da comparação.
    """

    coordenadas: np.ndarray
    conectividade: np.ndarray

    def __post_init__(self) -> None:
        """Valida os dados depois do __init__ gerado por dataclass."""
        if np.iscomplexobj(self.coordenadas):
            raise TypeError("As coordenadas devem ser reais.")
        coordenadas = np.array(self.coordenadas, dtype=float, copy=True)
        if coordenadas.ndim != 1 or coordenadas.size < 2:
            raise ValueError("As coordenadas devem ser um vetor com pelo menos dois nós.")
        if not np.all(np.isfinite(coordenadas)):
            raise ValueError("Todas as coordenadas devem ser finitas.")

        conectividade = np.asarray(self.conectividade)
        if conectividade.ndim != 2 or conectividade.shape[1] != 2:
            raise ValueError("A conectividade deve ter formato (numero_elementos, 2).")
        if conectividade.shape[0] == 0:
            raise ValueError("A malha deve conter pelo menos um elemento.")
        if not np.issubdtype(conectividade.dtype, np.integer):
            raise TypeError("A conectividade deve conter índices inteiros.")
        if np.any(conectividade < 0) or np.any(conectividade >= coordenadas.size):
            raise ValueError("A conectividade contém um índice fora do vetor de coordenadas.")

        # Copiar protege contra alterações involuntárias nos arrays recebidos.
        conectividade = np.array(conectividade, dtype=np.intp, copy=True)
        comprimentos = calcular_comprimentos(coordenadas, conectividade)
        if not np.all(np.isfinite(comprimentos)) or np.any(comprimentos <= 0):
            raise ValueError("Cada elemento deve ter comprimento finito e positivo.")

        self.coordenadas = coordenadas
        self.conectividade = conectividade

    def comprimentos(self) -> np.ndarray:
        """Retorna a diferença entre a coordenada final e a inicial de cada elemento."""
        return calcular_comprimentos(self.coordenadas, self.conectividade)


def criar_malha_uniforme(
    numero_elementos: int, comprimento: float = 1.0
) -> Malha1D:
    """Constrói elementos consecutivos no intervalo [0, comprimento].

    O número de elementos deve ser inteiro positivo; ``True`` e ``3.0`` não
    substituem um inteiro nesta interface. O comprimento deve ser real,
    finito e estritamente positivo.
    """
    if isinstance(numero_elementos, (bool, np.bool_)) or not isinstance(
        numero_elementos, (int, np.integer)
    ):
        raise TypeError("O número de elementos deve ser um inteiro, não bool ou float.")
    if numero_elementos <= 0:
        raise ValueError("O número de elementos deve ser positivo.")
    if isinstance(comprimento, (bool, np.bool_)) or not isinstance(comprimento, Real):
        raise TypeError("O comprimento deve ser um número real.")
    if not np.isfinite(comprimento) or comprimento <= 0:
        raise ValueError("O comprimento deve ser finito e positivo.")

    coordenadas = np.linspace(0.0, comprimento, numero_elementos + 1)
    nos_iniciais = np.arange(numero_elementos, dtype=np.intp)
    conectividade = np.column_stack((nos_iniciais, nos_iniciais + 1))
    return Malha1D(coordenadas, conectividade)
