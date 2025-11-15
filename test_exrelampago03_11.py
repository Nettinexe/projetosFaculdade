import pytest
from exerciciorelampago_03_11 import *

def test_escolaridade_presidente():
    esc = Escolaridade()
    esc.set_nome("Doutorado")

    pres = Funcionario()
    pres.set_nome("Dra. Grace Hopper")
    pres.set_escolaridade(esc)

    g = Grupo()
    g.set_nome("Grupo TI")
    g.set_presidente(pres)

    resultado = g.get_nome_presidente_escolaridade()

    assert resultado == "Doutorado"

def  test_pais_alocacao():
    pais_br = Pais()
    pais_br.set_nome("Brasil")
    
    grupo_x = Grupo()
    grupo_x.set_nome("Grupo X")
    grupo_x.set_sede(pais_br)

    empresa_y = Empresa()
    empresa_y.set_nome("Empresa Y")
    empresa_y.set_grupo(grupo_x)

    depto_rh = Departamento()
    depto_rh.set_nome("Recursos Humanos")
    depto_rh.set_empresa(empresa_y)

    func_ana = Funcionario()
    func_ana.set_nome("Ana")
    func_ana.set_alocacao(depto_rh)

    resultado = func_ana.get_nome_pais_alocacao()

    assert resultado == "Brasil"

def test_estado_coordenacao():
    pais_br = Pais()
    pais_br.set_nome("Brasil")

    estado_rj = Estado()
    estado_rj.set_nome("Rio de Janeiro")
    estado_rj.set_pais(pais_br)

    cidade_nit = Cidade()
    cidade_nit.set_nome("Niterói")
    cidade_nit.set_estado(estado_rj)

    filial_nit = Filial()
    filial_nit.set_nome("Filial Niterói")
    filial_nit.set_cidade(cidade_nit)

    func_bob = Funcionario()
    func_bob.set_nome("Bob")
    func_bob.set_coordenacao(filial_nit)

    resultado = func_bob.get_nome_estado_coordenacao()

    assert resultado == "Rio de Janeiro"

def test_escolaridade_chefe():
    esc = Escolaridade()
    esc.set_nome("Mestrado")

    chefe = Funcionario()
    chefe.set_nome("Chefe Alan")
    chefe.set_escolaridade(esc)

    depto = Departamento()
    depto.set_nome("TI")
    depto.set_chefia(chefe)

    resultado = depto.get_nome_escolaridade_chefe()

    assert resultado == "Mestrado"

def test_diretor_empresa_filial():
    diretor = Funcionario()
    diretor.set_nome("Diretor Carlos")

    empresa = Empresa()
    empresa.set_nome("Empresa Z")
    empresa.set_diretor(diretor)

    filial = Filial()
    filial.set_nome("Filial Centro")
    filial.set_empresa(empresa)

    resultado = filial.get_nome_diretor_empresa()

    assert resultado == "Diretor Carlos"