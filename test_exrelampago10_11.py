import pytest
from exrelampago10_11 import *

def test_pergunta_1_nome_professor_turma():
    c_ads = Curso("ADS")
    d_poo = Disciplina("POO")
    p_joao = Professor("Joao")
    t_ads_poo = Turma(p_joao, d_poo, c_ads)
    
    resultado = t_ads_poo.get_nome_professor()
    assert resultado == "Joao"

def test_pergunta_2_nomes_alunos_turma():
    c_ads = Curso("ADS")
    d_poo = Disciplina("POO")
    p_joao = Professor("Joao")
    a_ana = Aluno("Ana", c_ads)
    a_bruno = Aluno("Bruno", c_ads)
    t_ads_poo = Turma(p_joao, d_poo, c_ads)
    t_ads_poo.add_aluno(a_ana)
    t_ads_poo.add_aluno(a_bruno)

    resultado = t_ads_poo.get_nome_alunos()
    assert "Ana" in resultado
    assert "Bruno" in resultado
    assert len(resultado) == 2

def test_pergunta_3_nomes_professores_curso():
    c_ads = Curso("ADS")
    d_poo = Disciplina("POO")
    d_bd = Disciplina("Banco de Dados")
    p_joao = Professor("Joao")
    p_maria = Professor("Maria")
    t_ads_poo = Turma(p_joao, d_poo, c_ads)
    t_ads_bd = Turma(p_maria, d_bd, c_ads)

    resultado = c_ads.get_nome_prof()
    assert "Joao" in resultado
    assert "Maria" in resultado
    assert len(resultado) == 2

def test_pergunta_4_nomes_alunos_turmas_curso():
    c_ads = Curso("ADS")
    d_poo = Disciplina("POO")
    p_joao = Professor("Joao")
    a_ana = Aluno("Ana", c_ads)
    a_bruno = Aluno("Bruno", c_ads)
    a_daniel = Aluno("Daniel", c_ads)
    t_ads_poo = Turma(p_joao, d_poo, c_ads)
    t_ads_poo.add_aluno(a_ana)
    t_ads_poo.add_aluno(a_bruno)

    resultado = c_ads.get_nome_aluno()
    assert "Ana" in resultado
    assert "Bruno" in resultado
    assert "Daniel" not in resultado
    assert len(resultado) == 2

def test_pergunta_5_nomes_alunos_registrados_curso():
    c_ads = Curso("ADS")
    a_ana = Aluno("Ana", c_ads)
    a_bruno = Aluno("Bruno", c_ads)
    a_daniel = Aluno("Daniel", c_ads)

    resultado = c_ads.get_nome_alunos_registrados()
    assert "Ana" in resultado
    assert "Bruno" in resultado
    assert "Daniel" in resultado
    assert len(resultado) == 3

def test_pergunta_6_disciplinas_curso():
    c_ads = Curso("ADS")
    d_poo = Disciplina("POO")
    d_bd = Disciplina("Banco de Dados")
    p_joao = Professor("Joao")
    t_ads_poo = Turma(p_joao, d_poo, c_ads)
    t_ads_bd = Turma(p_joao, d_bd, c_ads)

    resultado = c_ads.get_disciplina_do_curso()
    assert "POO" in resultado
    assert "Banco de Dados" in resultado
    assert len(resultado) == 2

def test_pergunta_7_verificar_aluno_turma():
    c_ads = Curso("ADS")
    d_poo = Disciplina("POO")
    p_joao = Professor("Joao")
    a_ana = Aluno("Ana", c_ads)
    a_bruno = Aluno("Bruno", c_ads)
    t_ads_poo = Turma(p_joao, d_poo, c_ads)
    t_ads_poo.add_aluno(a_ana)
    
    assert t_ads_poo.verificar_aluno(a_ana) == True
    assert t_ads_poo.verificar_aluno(a_bruno) == False

def test_pergunta_8_verificar_aluno_curso():
    c_ads = Curso("ADS")
    c_eng = Curso("Engenharia")
    a_ana = Aluno("Ana", c_ads)
    a_carla = Aluno("Carla", c_eng)
    
    assert c_ads.verificar_aluno(a_ana) == True
    assert c_ads.verificar_aluno(a_carla) == False

def test_pergunta_9_verificar_turma_curso():
    c_ads = Curso("ADS")
    c_eng = Curso("Engenharia")
    d_poo = Disciplina("POO")
    d_calculo = Disciplina("Calculo")
    p_joao = Professor("Joao")
    p_maria = Professor("Maria")
    t_ads_poo = Turma(p_joao, d_poo, c_ads)
    t_eng_calc = Turma(p_maria, d_calculo, c_eng)
    
    assert c_ads.verificar_turma(t_ads_poo) == True
    assert c_ads.verificar_turma(t_eng_calc) == False

def test_pergunta_10_excluir_aluno_turma():
    c_ads = Curso("ADS")
    d_poo = Disciplina("POO")
    p_joao = Professor("Joao")
    a_ana = Aluno("Ana", c_ads)
    t_ads_poo = Turma(p_joao, d_poo, c_ads)
    t_ads_poo.add_aluno(a_ana)
    
    assert t_ads_poo.verificar_aluno(a_ana) == True
    assert t_ads_poo in a_ana.get_turmas()

    t_ads_poo.excluir_aluno(a_ana)
    
    assert t_ads_poo.verificar_aluno(a_ana) == False
    assert t_ads_poo not in a_ana.get_turmas()

def test_pergunta_11_excluir_turma_curso():
    c_ads = Curso("ADS")
    d_poo = Disciplina("POO")
    p_joao = Professor("Joao")
    t_ads_poo = Turma(p_joao, d_poo, c_ads)
    
    assert c_ads.verificar_turma(t_ads_poo) == True
    assert t_ads_poo.get_curso() == c_ads
    
    c_ads.excluir_turma(t_ads_poo)
    
    assert c_ads.verificar_turma(t_ads_poo) == False
    assert t_ads_poo.get_curso() == None

def test_pergunta_12_excluir_aluno_curso():
    c_ads = Curso("ADS")
    a_ana = Aluno("Ana", c_ads)
    
    assert c_ads.verificar_aluno(a_ana) == True
    assert a_ana.get_curso() == c_ads
    
    c_ads.excluir_aluno(a_ana)
    
    assert c_ads.verificar_aluno(a_ana) == False
    assert a_ana.get_curso() == None