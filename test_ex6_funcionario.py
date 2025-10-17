import pytest
from ex6 import Funcionario

def test_aumento_e_departamento():
    f = Funcionario()
    f._salario = 1000.0
    f._departamento = "Antigo"

    # aumento percentual simples
    f.receber_aumento(10)  # +10%
    assert f._salario == 1100.0

    # trocar departamento
    f.mudar_departamento("Novo")
    assert f._departamento == "Novo"

def test_exibir_dados_nao_levanta_erro(capsys):
    f = Funcionario()
    f._nome = "Ana"
    f._cargo = "Dev"
    f._salario = 2000.0
    f._departamento = "Engenharia"

    # função imprime; apenas checamos que não quebra e retorna as linhas esperadas
    f.exibir_dados()
    out = capsys.readouterr().out
    assert "Nome: Ana" in out
    assert "Cargo: Dev" in out
    assert "Salário: 2000.0" in out
    assert "Departamento: Engenharia" in out
