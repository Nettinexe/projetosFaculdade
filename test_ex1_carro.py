import pytest
from ex1 import Carro

def test_fluxo_basico_ligar_acelerar_frear_desligar():
    c = Carro()
    # estado inicial
    assert c.get_velocidade_atual() == 0
    assert c.get_ligado() is False

    # não acelera desligado
    c.acelerar(10)
    assert c.get_velocidade_atual() == 0

    # ligar
    c.ligar()
    assert c.get_ligado() is True

    # acelerar válido
    c.acelerar(30)
    assert c.get_velocidade_atual() == 30

    # frear não pode passar de 0
    c.frear(1000)
    assert c.get_velocidade_atual() == 0

    # só desliga se velocidade == 0
    c.desligar()
    assert c.get_ligado() is False

def test_validacoes_basicas():
    c = Carro()
    c.ligar()
    c.acelerar(0)  # zero é permitido conforme implementação (no-op)
    assert c.get_velocidade_atual() == 0
    c.acelerar(5)
    assert c.get_velocidade_atual() == 5
    c.frear(2)
    assert c.get_velocidade_atual() == 3
