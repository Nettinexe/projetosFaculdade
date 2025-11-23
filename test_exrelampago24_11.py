import pytest
from datetime import date
from exrelampago24_11 import *

@pytest.fixture
def cargo_padrao():
    return Cargo(2000.0)

@pytest.fixture
def funcionario_teste(cargo_padrao):
    return Funcionario("João da Silva", cargo_padrao)

def test_salario_inicial_sem_ocorrencias(funcionario_teste):
    salario = funcionario_teste.calcularSalarioLiquido(10, 2025)
    assert salario == 2000.0

def test_salario_com_acrescimo_mes_correto(funcionario_teste):
    oc = Ocorrencia(date(2025, 10, 15), 500.0, 0.0, "Bônus Meta")
    funcionario_teste.adicionar_ocorrencia(oc)
    salario = funcionario_teste.calcularSalarioLiquido(10, 2025)
    assert salario == 2500.0

def test_salario_com_desconto_mes_correto(funcionario_teste):
    oc = Ocorrencia(date(2025, 10, 20), 0.0, 200.0, "Falta injustificada")
    funcionario_teste.adicionar_ocorrencia(oc)
    salario = funcionario_teste.calcularSalarioLiquido(10, 2025)
    assert salario == 1800.0

def test_ignora_ocorrencia_mes_errado(funcionario_teste):
    oc = Ocorrencia(date(2025, 1, 15), 1000.0, 0.0, "Bônus antigo")
    funcionario_teste.adicionar_ocorrencia(oc)
    salario = funcionario_teste.calcularSalarioLiquido(10, 2025)
    assert salario == 2000.0

def test_salario_com_dependente_menor_idade(funcionario_teste):
    filho = Dependente(date(2020, 5, 10), "Filho Jr")
    funcionario_teste.adicionar_dependente(filho)
    salario = funcionario_teste.calcularSalarioLiquido(10, 2025)
    assert salario == 2100.0

def test_salario_sem_bonus_dependente_maior_idade(funcionario_teste):
    filho_adulto = Dependente(date(2000, 1, 1), "Filho Adulto")
    funcionario_teste.adicionar_dependente(filho_adulto)
    salario = funcionario_teste.calcularSalarioLiquido(10, 2025)
    assert salario == 2000.0

def test_cenario_complexo(funcionario_teste):
    oc1 = Ocorrencia(date(2025, 12, 1), 300.0, 0.0, "Bônus Natal")
    funcionario_teste.adicionar_ocorrencia(oc1)
    oc2 = Ocorrencia(date(2025, 1, 1), 5000.0, 0.0, "Erro")
    funcionario_teste.adicionar_ocorrencia(oc2)
    dep = Dependente(date(2015, 1, 1), "Criança")
    funcionario_teste.adicionar_dependente(dep)
    salario = funcionario_teste.calcularSalarioLiquido(12, 2025)
    assert salario == 2400.0