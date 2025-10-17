import pytest
from ex2 import ContaBancaria

def test_deposito_saque_ok():
    conta = ContaBancaria()
    assert conta.get_saldo() == 0

    conta.depositar(100)
    assert conta.get_saldo() == 100

    # saque possível
    conta.sacar(60)
    assert conta.get_saldo() == 40

def test_saque_invalido():
    conta = ContaBancaria()
    conta.depositar(50)
    # não saca acima do saldo
    conta.sacar(999)
    assert conta.get_saldo() == 50
    # não saca valor negativo/zero
    conta.sacar(0)
    assert conta.get_saldo() == 50
