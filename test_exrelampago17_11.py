import pytest
from exrelampago17_11 import *

def test_estoque_baixo_verdadeiro():
    produto = Produto("Caderno", 5, 20.0, 10, 100)
    verificarEstBx = produto.verificarEstoqueBaixo()

    assert verificarEstBx is True

def test_estoque_baixo_falso():
    produto = Produto("Caderno", 15, 20.0, 10, 100)
    verificarEstBx = produto.verificarEstoqueBaixo()

    assert verificarEstBx is False

def test_venda_sucesso_e_debito():
    cliente = Cliente("Eduardo", 13300125693)
    produto = Produto("Caderno", 15, 20.0, 10, 100)
    produto.vender("01/01/2025", cliente, 10)

    assert produto.get_qtdeEstoque() == 5

def test_venda_falha_sem_debito():
    cliente = Cliente("Eduardo", 13300125693)
    produto = Produto("Caderno", 10, 20.0, 10, 100)
    venda = produto.vender("01/01/2025", cliente, 15)

    assert venda is False 
    assert produto.get_qtdeEstoque() == 10

def test_compra_falha_por_excedente():
    fornecedor = Fornecedor("NTTsolutions", 11111111111111)
    produto = Produto("Caderno", 90, 20.0, 10, 100)
    compra = produto.comprar("01/01/2025", fornecedor, 15, 5.0)

    assert compra is False
    assert produto.get_qtdeEstoque() == 90
    
def test_compra_sucesso_e_credito():
    fornecedor = Fornecedor("NTTsolutions", 11111111111111)
    produto = Produto("Caderno", 10, 20.0, 10, 100)
    compra = produto.comprar("01/01/2025", fornecedor, 50, 5.0)

    assert compra is True
    assert produto.get_qtdeEstoque() == 60