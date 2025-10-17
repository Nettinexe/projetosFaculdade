import pytest
from ex5 import Produto

def test_estoque_e_desconto():
    pr = Produto()
    # define dados iniciais diretamente conforme estrutura do exercício
    pr._preco = 100.0
    pr._quantidade_estoque = 10

    pr.adicionar_estoque(5)
    assert pr._quantidade_estoque == 15

    # remover até o limite
    pr.remover_estoque(4)
    assert pr._quantidade_estoque == 11

    # remover acima do disponível não altera
    pr.remover_estoque(999)
    assert pr._quantidade_estoque == 11

    # aplicar desconto percentual (0 < p <= 100)
    pr.aplicar_desconto(10)
    assert pr._preco == 90.0

def test_desconto_limite():
    pr = Produto()
    pr._preco = 50.0
    pr.aplicar_desconto(100)  # permitido (vira 0.0 na implementação atual)
    assert pr._preco == 0.0
