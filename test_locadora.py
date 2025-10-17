import pytest
from locadora import Veiculo, Automovel, Onibus

def test_alugar_automovel_sucesso():
    a = Automovel()
    assert a.alugar() == "Veículo alugado com sucesso!"
    assert a.get_estado() == "alugado"
    assert a.get_qntdalg() == 1

def test_alugar_automovel_ja_alugado():
    a = Automovel()
    a.alugar()
    assert a.alugar() == "Este veículo está alugado!"
    assert a.get_qntdalg() == 1  

def test_devolver_sem_atraso_automovel():
    a = Automovel()
    a.alugar()
    mensagem = a.devolver(6) 
    assert a.get_estado() == "disponivel"
    assert mensagem == "! Multa: R$0.00"

def test_devolver_com_atraso_automovel():
    a = Automovel()
    a.alugar()
    mensagem = a.devolver(10)  
    assert a.get_estado() == "disponivel"
    assert mensagem == "! Multa: R$200.00"

def test_devolver_veiculo_nao_alugado():
    a = Automovel()
    mensagem = a.devolver(5)
    assert mensagem == "Este carro não foi alugado"

def test_onibus_multas():
    b = Onibus()
    b.alugar()
    mensagem = b.devolver(15) 
    assert mensagem == "! Multa: R$1000.00"

def test_qntdalg_incrementa():
    a = Automovel()
    a.alugar()
    a.devolver(5)
    a.alugar()
    assert a.get_qntdalg() == 2
