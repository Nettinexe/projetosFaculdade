class Pessoa:
    def __init__(self, nome):
        self._nome = nome
    def set_nome(self, nome):
        self._nome = nome
    def get_nome(self):
        return self._nome

class Aluno(Pessoa):
    def __init__(self, nome, curso):
        super().__init__(nome)
        self._curso = curso
        self._turmas = []
        curso.add_aluno(self) # <-- CORREÇÃO ADICIONADA
        
    def set_curso(self, curso):
        self._curso = curso
    def get_curso(self):
        return self._curso
    def set_turmas(self, turmas):
        self._turmas= turmas
    def get_turmas(self):
        return self._turmas
    def add_turmas(self, turma):
        if turma not in self._turmas:
            self._turmas.append(turma)
            turma.add_aluno(self)
    
    def excluir_turmas(self, turma):
        if turma in self._turmas:
            self._turmas.remove(turma)
            turma.excluir_aluno(self)

    
class Turma:
    def __init__(self, professor, disciplina, curso):
        self._professor = professor
        self._disciplina = disciplina
        self._alunos = []
        self._curso = curso
        professor.add_turma(self) # <-- CORREÇÃO ADICIONADA
        curso.add_turma(self)     # <-- CORREÇÃO ADICIONADA
        
    def set_professor(self, professor):
        self._professor = professor
    def get_professor(self):
        return self._professor
    def set_disciplina(self, disciplina):
        self._disciplina = disciplina
    def get_disciplina(self):
        return self._disciplina
    def set_alunos(self, alunos):
        self._alunos = alunos
    def get_alunos(self):
        return self._alunos
    def set_curso(self, curso):
        self._curso = curso
    def get_curso(self):
        return self._curso
    def add_aluno(self, aluno):
        if aluno not in self._alunos:
            self._alunos.append(aluno)
            aluno.add_turmas(self)

    def excluir_aluno(self, aluno):
        if aluno in self._alunos:
            self._alunos.remove(aluno)
            aluno.excluir_turmas(self)
            
    def get_nome_professor(self):
        return self._professor.get_nome()
        
    def get_nome_alunos(self):
        lista_nomes = []
        for aluno in self._alunos:
            nome_aluno = aluno.get_nome()
            lista_nomes.append(nome_aluno)
        return lista_nomes
        
    def verificar_aluno(self, aluno):
        return aluno in self._alunos
            
class Disciplina:
    def __init__(self, nome):
        self._nome = nome
    def set_nome(self, nome):
        self._nome = nome
    def get_nome(self):
        return self._nome
        
class Curso:
    def __init__(self, nome):
        self._nome = nome
        self._alunos = []
        self._turmas = []
    def set_nome(self, nome):
        self._nome = nome
    def get_nome(self):
        return self._nome
    def set_alunos(self, aluno):
        self._alunos = aluno
    def get_alunos(self):
        return self._alunos
    def set_turmas(self, turma):
        self._turmas = turma
    def get_turmas(self):
        return self._turmas
        
    def add_turma(self, turma):
        if turma not in self._turmas:
            self._turmas.append(turma)
            turma.set_curso(self)
        else:
            return "Turma já inserida no curso"
            
    def add_aluno(self, aluno):
        if aluno not in self._alunos:
            self._alunos.append(aluno)
            aluno.set_curso(self)
        else:
            return "Aluno já inserido no curso"
            
    def get_nome_prof(self):
        nome_prof = []
        for turma in self._turmas:
            prof = turma.get_professor()
            nm_prof = prof.get_nome()
            if nm_prof not in nome_prof:
                nome_prof.append(nm_prof)
        return nome_prof
        
    def get_nome_aluno(self):
        nome_aluno = []
        for turma in self._turmas:
            alunos = turma.get_alunos()
            for aluno in alunos:
                nm_aluno = aluno.get_nome()
                if nm_aluno not in nome_aluno:
                    nome_aluno.append(nm_aluno)
        return nome_aluno
        
    def get_nome_alunos_registrados(self):
        lista_nomes = []
        for aluno in self._alunos:
            nome = aluno.get_nome()
            lista_nomes.append(nome)
        return lista_nomes
        
    def get_disciplina_do_curso(self):
        lista_nomes = []
        for turma in self._turmas:
            disciplina = turma.get_disciplina()
            nome_disciplina = disciplina.get_nome()
            if nome_disciplina not in lista_nomes:
                lista_nomes.append(nome_disciplina)
        return lista_nomes
        
    def verificar_aluno(self, aluno):
        return aluno in self._alunos
        
    def verificar_turma(self, turma):
        return turma in self._turmas
        
    def excluir_turma(self, turma):
        if turma in self._turmas:
            self._turmas.remove(turma)
            turma.set_curso(None)
            
    def excluir_aluno(self, aluno):
        if aluno in self._alunos:
            self._alunos.remove(aluno)
            aluno.set_curso(None)

class Professor(Pessoa):
    def __init__(self, nome):
        super().__init__(nome)
        self._turmas = []
    def set_turmas(self, turma):
        self._turmas = turma
    def get_turmas(self):
        return self._turmas
    def add_turma(self, turma):
        if turma not in self._turmas:
            self._turmas.append(turma)
            turma.set_professor(self)
        else:
            return "Professor já alocado"