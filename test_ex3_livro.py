import pytest
from ex3 import Livro

def test_marcar_avancar_retroceder():
    l = Livro()
    # configura metadados via atributos internos (exercício usa atributos simples)
    # define livro com 10 páginas
    l._numero_paginas = 10

    # abrir e marcar página válida
    l.abrir()
    l.marcar_pagina(3)
    assert l._pagina_atual == 3

    # avançar até o limite
    for _ in range(10):
        l.avancar_pagina()
    assert l._pagina_atual == 10  # não ultrapassa

    # retroceder até limite
    for _ in range(20):
        l.retroceder_pagina()
    assert l._pagina_atual == 1  # não vai abaixo de 1

def test_fechar_e_abrir():
    l = Livro()
    l._numero_paginas = 5
    l.abrir()
    assert l._aberto is True
    l.fechar()
    assert l._aberto is False
