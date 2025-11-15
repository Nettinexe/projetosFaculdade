class Estado:
    def __init__(self):
        self.nome = ""
    def get_nome(self):
        return self.nome
    def set_nome(self, nome):
        self.nome = nome

class Cidade:
    def __init__(self, estado):
        self.estado = estado
    def set_estado(self, estado):
        self.estado = estado
    def get_estado(self):
        return self.estado
    def get_nome_estado(self):
        return self.estado.get_nome()

class Escolaridade:
    def __init__(self):
        self.nome = ""
    def set_nome(self, nome):
        self.nome = nome
    def get_nome(self):
        return self.nome

class Pessoa:
    def __init__(self):
        self.nome = ""
        self.escolaridade = None
        self.naturalidade = None
    def set_nome(self, nome):
        self.nome = nome
    def get_nome(self):
        return self.nome
    def set_escolaridade(self, escolaridade):
        self.escolaridade = escolaridade
    def get_escolaridade(self):
        return self.escolaridade
    def set_naturalidade(self, naturalidade):
        self.naturalidade = naturalidade
    def get_naturalidade(self):
        return self.naturalidade
    def get_nome_escolaridade(self):
        if self.escolaridade == None:
            return "Pessoa sem escolaridade"
        else:
            return self.escolaridade.get_nome()
    def get_nome_estado_naturalidade(self):
        if self.naturalidade == None:
            return "Pessoa sem naturalidade"
        else:
            return self.naturalidade.get_nome_estado()

class Professor(Pessoa):
    def __init__(self):
        Pessoa.__init__(self)
        self.curso = None
    def set_curso(self, curso):
        self.curso = curso
    def get_curso(self):
        return self.curso
    def get_nome_coordenador(self):
        if self.curso == None:
            return "Professor sem curso"
        else:
            return self.curso.get_nome_coordenador()
    def get_nome_diretor(self):
        if self.curso == None:
            return "Professor sem curso"
        else:
            return self.curso.get_nome_diretor()


class Aluno(Pessoa):
    def __init__(self):
        Pessoa.__init__(self)

class Curso:
    def __init__(self):
        self.coordenador = None
        self.escola = None
    def get_coordenador(self):
        return self.coordenador
    def set_coordenador(self, coordenador):
        self.coordenador = coordenador
    def get_escola(self):
        return self.escola
    def set_escola(self, escola):
        self.escola = escola
    def get_nome_diretor(self):
        if self.escola == None:
            return "Curso sem escola"
        else:
            return self.escola.get_nome_diretor()
    def get_nome_coordenador(self):
        if self.coordenador == None:
            return "Curso sem coordenador"
        else:
            return self.coordenador.get_nome()

class Escola:
    def __init__(self):
        self.diretor = None
    def get_diretor(self):
        return self.diretor
    def set_diretor(self, diretor):
        self.diretor = diretor
    def get_nome_diretor(self):
        if self.diretor == None:
            return "Escola sem diretor"
        else:
            return self.diretor.get_nome()