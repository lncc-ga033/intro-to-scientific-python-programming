"""Uma função pequena para praticar a importação de um módulo Python."""

import numpy as np


def calcular_comprimentos(
    coordenadas: np.ndarray, conectividade: np.ndarray
) -> np.ndarray:
    """Calcula comprimentos a partir de arrays de coordenadas e índices válidos.

    Cada linha da conectividade contém os índices inicial e final de um
    elemento. A validação da estrutura é responsabilidade de quem chama a
    função; a classe Malha1D mostra uma maneira de fazê-la.
    """
    nos_iniciais = conectividade[:, 0]
    nos_finais = conectividade[:, 1]
    return coordenadas[nos_finais] - coordenadas[nos_iniciais]
