# test_biblioteca.py
import pytest
from exrevisao import Livro, Periodico

# --------- Fixtures ----------
@pytest.fixture
def livro():
    return Livro()

@pytest.fixture
def periodico():
    return Periodico()

# --------- Testes de emprestar ----------
def test_emprestar_disponivel_incrementa_contador_e_muda_estado(livro):
    assert livro.get_estado() == "disponivel"
    assert livro.get_qntdemp() == 0

    msg = livro.emprestar()
    assert msg == "Livro emprestado com sucesso!"
    assert livro.get_estado() == "emprestado"
    assert livro.get_qntdemp() == 1

def test_emprestar_ja_emprestado_nao_incrementa_nem_muda_estado(livro):
    livro.emprestar()
    qnt_antes = livro.get_qntdemp()
    estado_antes = livro.get_estado()

    msg = livro.emprestar()
    assert "Este livro não está disponível no momento" in msg
    assert livro.get_qntdemp() == qnt_antes
    assert livro.get_estado() == estado_antes

# --------- Testes de devolver (sem atraso) ----------
@pytest.mark.parametrize(
    "factory,dias_uso",
    [
        (Livro, 6),       # prazo do livro
        (Periodico, 10),  # prazo do periódico
    ],
)
def test_devolver_sem_atraso_nao_gera_multa(factory, dias_uso):
    obra = factory()
    obra.emprestar()
    msg = obra.devolver(dias_uso)
    assert "Multa: R$0.00" in msg
    assert obra.get_estado() == "disponivel"

# --------- Testes de devolver (com atraso) ----------
@pytest.mark.parametrize(
    "factory,dias_uso,multa_esperada",
    [
        (Livro, 8, 10.00),        # 2 dias de atraso * 5.0
        (Periodico, 12, 4.00),    # 2 dias de atraso * 2.0
        (Livro, 7, 5.00),         # 1 dia de atraso * 5.0
        (Periodico, 15, 10.00),   # 5 dias de atraso * 2.0
    ],
)
def test_devolver_com_atraso_calcula_multa_correta(factory, dias_uso, multa_esperada):
    obra = factory()
    obra.emprestar()
    msg = obra.devolver(dias_uso)
    assert f"Multa: R${multa_esperada:.2f}" in msg
    assert obra.get_estado() == "disponivel"

# --------- Devolver quando não está emprestado ----------
@pytest.mark.parametrize("factory", [Livro, Periodico])
def test_devolver_quando_nao_emprestado(factory):
    obra = factory()
    assert obra.get_estado() == "disponivel"
    msg = obra.devolver(5)
    assert "Este livro não foi emprestado" in msg
    assert obra.get_estado() == "disponivel"

# --------- Getters/Setters básicos ----------
def test_getters_setters_basicos(livro):
    livro.set_titulo("Dom Casmurro")
    livro.set_autor("Machado de Assis")
    livro.set_ano(1899)
    livro.set_editora("Garnier")

    assert livro.get_titulo() == "Dom Casmurro"
    assert livro.get_autor() == "Machado de Assis"
    assert livro.get_ano() == 1899
    assert livro.get_editora() == "Garnier"
