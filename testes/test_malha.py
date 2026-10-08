"""Verificações das garantias da estrutura de malha usada no curso."""

import numpy as np
import pytest

from exemplos.calculos import calcular_comprimentos
from exemplos.malha import Malha1D, criar_malha_uniforme


def test_funcao_calcula_comprimentos_nao_uniformes():
    coordenadas = np.array([0.0, 0.2, 0.7, 1.0])
    conectividade = np.array([[0, 1], [1, 2], [2, 3]])
    np.testing.assert_allclose(
        calcular_comprimentos(coordenadas, conectividade), [0.2, 0.5, 0.3]
    )


def test_malha_sem_elementos_e_recusada():
    with pytest.raises(ValueError, match="pelo menos um elemento"):
        Malha1D([0.0, 1.0], np.empty((0, 2), dtype=int))


def test_uniforme_tem_conectividade_e_comprimentos_esperados():
    malha = criar_malha_uniforme(4, comprimento=2.0)
    np.testing.assert_allclose(malha.coordenadas, [0.0, 0.5, 1.0, 1.5, 2.0])
    np.testing.assert_array_equal(malha.conectividade, [[0, 1], [1, 2], [2, 3], [3, 4]])
    np.testing.assert_allclose(malha.comprimentos(), 0.5)
    assert np.isclose(malha.comprimentos().sum(), 2.0)


def test_malha_copia_os_arrays_recebidos():
    coordenadas = np.array([0.0, 0.3, 1.0])
    conectividade = np.array([[0, 1], [1, 2]])
    malha = Malha1D(coordenadas, conectividade)
    coordenadas[1] = 0.9
    conectividade[0, 1] = 2
    np.testing.assert_allclose(malha.comprimentos(), [0.3, 0.7])
    np.testing.assert_array_equal(malha.conectividade, [[0, 1], [1, 2]])


@pytest.mark.parametrize("numero", [True, False, 3.0, 2.5, "3"])
def test_numero_de_elementos_exige_inteiro(numero):
    with pytest.raises(TypeError):
        criar_malha_uniforme(numero)


@pytest.mark.parametrize("numero", [0, -1])
def test_numero_de_elementos_deve_ser_positivo(numero):
    with pytest.raises(ValueError):
        criar_malha_uniforme(numero)


@pytest.mark.parametrize("comprimento", [0.0, -1.0, np.nan, np.inf])
def test_comprimento_uniforme_deve_ser_finito_e_positivo(comprimento):
    with pytest.raises(ValueError):
        criar_malha_uniforme(3, comprimento)


@pytest.mark.parametrize("coordenadas", [[0.0], [[0.0, 1.0]], [0.0, np.nan], [0.0, np.inf]])
def test_coordenadas_invalidas_sao_recusadas(coordenadas):
    with pytest.raises(ValueError):
        Malha1D(coordenadas, [[0, 1]])


@pytest.mark.parametrize("conectividade", [[0, 1], [[0, 1, 2]], [[-1, 1]], [[0, 3]]])
def test_formato_e_indices_invalidos_sao_recusados(conectividade):
    with pytest.raises(ValueError):
        Malha1D([0.0, 0.5, 1.0], conectividade)


@pytest.mark.parametrize("conectividade", [[[0.0, 1.0]], [[False, True]]])
def test_indices_nao_inteiros_sao_recusados(conectividade):
    with pytest.raises(TypeError):
        Malha1D([0.0, 1.0], conectividade)


@pytest.mark.parametrize("conectividade", [[[1, 0]], [[1, 1]]])
def test_elementos_invertidos_ou_de_comprimento_zero_sao_recusados(conectividade):
    with pytest.raises(ValueError):
        Malha1D([0.0, 1.0], conectividade)
