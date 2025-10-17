import pytest
from ex4 import Pessoa

def test_envelhecer_crescer_ganhar_perder_peso():
    p = Pessoa()
    # estado inicial neutro
    assert p._idade == 0
    assert p._altura == 0.0
    assert p._peso == 0.0

    # crescer só até 21 anos pela regra implementada
    p.crescer(10)  # idade < 21, pode crescer
    assert p._altura == 10

    # envelhecer aumenta idade
    p.envelhecer()
    assert p._idade == 1

    # ganho e perda de peso
    p.ganhar_peso(12.5)
    assert p._peso == 12.5
    p.perder_peso(2.5)
    assert p._peso == 10.0

    # não deixar peso negativo
    p.perder_peso(999)
    assert p._peso == 0.0
