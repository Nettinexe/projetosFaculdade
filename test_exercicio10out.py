import pytest
from exrelampago10out import *

def test_deve_retornar_escolaridade_professor():
    escolaridade = Escolaridade("Doutorado")
    professor = Professor("Ada")
    professor.set_escolaridade(escolaridade)
    assert professor.get_nome_escolaridade() == "Doutorado"

def test_deve_retornar_escolaridade_professor_invalido():
    professor = Professor("Alan")
    assert professor.get_nome_escolaridade() == "Pessoa sem escolaridade"

def test_deve_retornar_nome_estado_cidade():
    estado = Estado("MG")
    cidade = Cidade("Juiz de Fora", estado)
    assert cidade.get_nome_estado() == "MG"

def test_deve_retornar_estado_naturalidade_aluno():
    estado = Estado("MG")
    cidade = Cidade("Juiz de Fora", estado)
    aluno = Aluno("Bob")
    aluno.set_naturalidade(cidade)
    assert aluno.get_nome_estado_naturalidade() == "MG"

def test_deve_retornar_estado_naturalidade_aluno_invalido():
    aluno = Aluno("Grace")
    assert aluno.get_nome_estado_naturalidade() == "Pessoa sem naturalidade"

def test_b_escolaridade_coordenador_curso():
    escolaridade_coord = Escolaridade("Mestrado")
    coordenador = Professor("Prof. Coordenador")
    coordenador.set_escolaridade(escolaridade_coord)
    tipo_ensino = TipoEnsino("Superior")
    curso = Curso("Engenharia de Software", tipo_ensino)
    curso.set_coordenador(coordenador)
    
    assert curso.get_coordenador().get_nome_escolaridade() == "Mestrado"

def test_c_escolaridade_diretor_escola():
    estado = Estado("SP")
    cidade = Cidade("São Paulo", estado)
    escola = Escola("Escola Politécnica", cidade)
    escolaridade_diretor = Escolaridade("PhD")
    diretor = Professor("Prof. Diretor")
    diretor.set_escolaridade(escolaridade_diretor)
    escola.set_diretor(diretor)

    assert escola.get_diretor().get_nome_escolaridade() == "PhD"

def test_e_cidade_nascimento_professor():
    estado = Estado("RJ")
    cidade = Cidade("Niterói", estado)
    professor = Professor("Prof. Silva")
    professor.set_naturalidade(cidade)
    assert professor.get_nome_cidade_naturalidade() == "Niterói"

def test_e_cidade_nascimento_professor_invalido():
    professor = Professor("Prof. Silva")
    assert professor.get_nome_cidade_naturalidade() == "Pessoa sem naturalidade"

def test_f_estado_onde_aluno_estuda():
    estado_escola = Estado("PR")
    cidade_escola = Cidade("Curitiba", estado_escola)
    escola = Escola("Universidade Positivo", cidade_escola)
    tipo_ensino = TipoEnsino("Graduação")
    curso = Curso("Design Gráfico", tipo_ensino)
    aluno = Aluno("Maria")
    
    escola.add_curso(curso) 
    curso.add_aluno(aluno)  

    assert aluno.get_curso().get_escola().get_cidade().get_nome_estado() == "PR"

def test_g_tipo_ensino_professor():
    tipo_ensino = TipoEnsino("Pós-graduação")
    curso = Curso("IA Aplicada", tipo_ensino)
    professor = Professor("Dr. Xavier")
    
    curso.add_professor(professor)

    assert professor.get_cursos_lecionados()[0].get_tipo_ensino().get_nome() == "Pós-graduação"

def test_h_coordenador_curso_aluno():
    tipo_ensino = TipoEnsino("Técnico")
    curso = Curso("Redes de Computadores", tipo_ensino)
    coordenador = Professor("Prof. Antunes")
    aluno = Aluno("Felipe")

    curso.set_coordenador(coordenador)
    curso.add_aluno(aluno)

    assert aluno.get_curso().get_nome_coordenador() == "Prof. Antunes"

def test_h_coordenador_curso_aluno_invalido():
    tipo_ensino = TipoEnsino("Técnico")
    curso = Curso("Manutenção", tipo_ensino)
    aluno = Aluno("Mariana")
    
    curso.add_aluno(aluno) 

    assert aluno.get_curso().get_nome_coordenador() == "Curso sem coordenador"

def test_i_diretor_de_um_professor():
    estado = Estado("SC")
    cidade = Cidade("Florianópolis", estado)
    escola = Escola("UFSC", cidade)
    diretor = Professor("Prof. Diretor Silva")
    escola.set_diretor(diretor)
    
    tipo_ensino = TipoEnsino("Superior")
    curso = Curso("Engenharia Civil", tipo_ensino)
    professor = Professor("Profa. Beatriz")
    
    escola.add_curso(curso)
    curso.add_professor(professor)

    assert professor.get_cursos_lecionados()[0].get_escola().get_nome_diretor() == "Prof. Diretor Silva"

def test_i_diretor_de_um_professor_invalido():
    estado = Estado("SC")
    cidade = Cidade("Florianópolis", estado)
    escola = Escola("UFSC", cidade)
    
    tipo_ensino = TipoEnsino("Superior")
    curso = Curso("Engenharia Civil", tipo_ensino)
    professor = Professor("Profa. Beatriz")
    
    escola.add_curso(curso)
    curso.add_professor(professor)

    # CORREÇÃO AQUI: get_cursos_lecionais -> get_cursos_lecionados
    assert professor.get_cursos_lecionados()[0].get_escola().get_nome_diretor() == "Escola sem diretor"

def test_j_coordenador_de_um_professor():
    tipo_ensino = TipoEnsino("Superior")
    curso = Curso("Medicina", tipo_ensino)
    coordenador = Professor("Dr. House")
    professor_aula = Professor("Dr. Wilson")
    
    curso.set_coordenador(coordenador)
    curso.add_professor(professor_aula)

    assert professor_aula.get_cursos_lecionados()[0].get_nome_coordenador() == "Dr. House"

def test_j_coordenador_de_um_professor_invalido():
    tipo_ensino = TipoEnsino("Superior")
    curso = Curso("Medicina", tipo_ensino)
    professor_aula = Professor("Dr. Wilson")
    
    curso.add_professor(professor_aula) 

    assert professor_aula.get_cursos_lecionados()[0].get_nome_coordenador() == "Curso sem coordenador"