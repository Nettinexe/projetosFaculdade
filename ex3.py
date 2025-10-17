# 3. Classe Livro
class Livro:
    def __init__(self):
        self._titulo = ""
        self._autor = ""
        self._ano_publicacao = 0
        self._numero_paginas = 0
        self._genero = ""
        self._pagina_atual = 0
        self._aberto = False

    def abrir(self):
        self._aberto = True
        print("O livro foi aberto.")

    def fechar(self):
        self._aberto = False
        print("O livro foi fechado.")

    def marcar_pagina(self, pagina):
        if 0 < pagina <= self._numero_paginas:
            self._pagina_atual = pagina

    def avancar_pagina(self):
        if self._aberto and self._pagina_atual < self._numero_paginas:
            self._pagina_atual += 1

    def retroceder_pagina(self):
        if self._aberto and self._pagina_atual > 1:
            self._pagina_atual -= 1