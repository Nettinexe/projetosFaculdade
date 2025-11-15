class Estado:
    def __init__(self, nome):
        self.nome = nome
        
    def get_nome(self):
        return self.nome
        
    def set_nome(self, nome):
        self.nome = nome

class Cidade:
    def __init__(self, nome, estado):
        self.nome = nome
        self.estado = estado
        
    def set_estado(self, estado):
        self.estado = estado
        
    def get_estado(self):
        return self.estado
        
    def get_nome(self):
        return self.nome

    def get_nome_estado(self):
        return self.estado.get_nome()

class Escolaridade:
    def __init__(self, nome):
        self.nome = nome
        
    def set_nome(self, nome):
        self.nome = nome
        
    def get_nome(self):
        return self.nome

class TipoEnsino:
    def __init__(self, nome):
        self.nome = nome
        
    def get_nome(self):
        return self.nome
        
    def set_nome(self, nome):
        self.nome = nome

class Pessoa:
    def __init__(self, nome):
        self.nome = nome
        self.escolaridade = None
        self.naturalidade = None

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
        if self.escolaridade is None:
            return "Pessoa sem escolaridade"
        else:
            return self.escolaridade.get_nome()
        
    def get_nome_estado_naturalidade(self):
        if self.naturalidade is None:
            return "Pessoa sem naturalidade"
        else:
            return self.naturalidade.get_nome_estado()

    def get_nome_cidade_naturalidade(self):
        if self.naturalidade is None:
            return "Pessoa sem naturalidade"
        else:
            return self.naturalidade.get_nome()

class Professor(Pessoa):
    def __init__(self, nome):
        super().__init__(nome)
        self.cursos_lecionados = [] 
        self.escola_dirigida = None
        self.curso_coordenado = None

    def add_curso_lecionado(self, curso):
        if curso not in self.cursos_lecionados:
            self.cursos_lecionados.append(curso)
            if self not in curso.get_professores():
                curso.add_professor(self) 

    def get_cursos_lecionados(self):
        return self.cursos_lecionados

    def set_escola_dirigida(self, escola):
        self.escola_dirigida = escola
        if escola.get_diretor() != self:
            escola.set_diretor(self)
        
    def get_escola_dirigida(self):
        return self.escola_dirigida

    def set_curso_coordenado(self, curso):
        self.curso_coordenado = curso
        if curso.get_coordenador() != self:
            curso.set_coordenado(self)
        
    def get_curso_coordenado(self):
        return self.curso_coordenado

class Aluno(Pessoa):
    def __init__(self, nome):
        super().__init__(nome)
        self.curso = None

    def set_curso(self, curso):
        self.curso = curso
        if self not in curso.get_alunos():
            curso.add_aluno(self)

    def get_curso(self):
        return self.curso

class Curso:
    def __init__(self, nome, tipo_ensino):
        self.nome = nome
        self.tipo_ensino = tipo_ensino
        self.coordenador = None
        self.escola = None
        self.alunos = []
        self.professores = []

    def get_nome(self):
        return self.nome

    def get_tipo_ensino(self):
        return self.tipo_ensino

    def set_coordenador(self, professor):
        self.coordenador = professor
        if professor.get_curso_coordenado() != self:
            professor.set_curso_coordenado(self) 

    def get_coordenador(self):
        return self.coordenador

    def set_escola(self, escola):
        self.escola = escola
        if self not in escola.get_cursos():
             escola.add_curso(self) 

    def get_escola(self):
        return self.escola

    def add_aluno(self, aluno):
        if aluno not in self.alunos:
            self.alunos.append(aluno)
            aluno.set_curso(self) 
            
    def get_alunos(self):
        return self.alunos
        
    def add_professor(self, professor):
        if professor not in self.professores:
            self.professores.append(professor)
            professor.add_curso_lecionado(self) 

    def get_professores(self):
        return self.professores

    def get_nome_coordenador(self):
        if self.coordenador:
            return self.coordenador.get_nome()
        return "Curso sem coordenador"

class Escola:
    def __init__(self, nome, cidade):
        self.nome = nome
        self.cidade = cidade
        self.diretor = None
        self.cursos = []

    def get_nome(self):
        return self.nome

    def set_diretor(self, professor):
        self.diretor = professor
        if professor.get_escola_dirigida() != self:
            professor.set_escola_dirigida(self) 

    def get_diretor(self):
        return self.diretor
        
    def get_nome_diretor(self):
        if self.diretor:
            return self.diretor.get_nome()
        return "Escola sem diretor"

    def add_curso(self, curso):
        if curso not in self.cursos:
            self.cursos.append(curso)
            curso.set_escola(self) 
            
    def get_cursos(self):
        return self.cursos

    def get_cidade(self):
        return self.cidade