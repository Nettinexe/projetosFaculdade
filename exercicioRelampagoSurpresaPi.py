# --- 1. DEFINIÇÃO DAS CLASSES ---
# Baseado no diagrama UML e no código inicial fornecido

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
        self.estado = estado  # Associação com Estado (1)
        
    def set_estado(self, estado):
        self.estado = estado
        
    def get_estado(self):
        return self.estado
        
    def get_nome(self):
        return self.nome

    def get_nome_estado(self):
        # Delegação: Pede o nome ao objeto Estado
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
        self.escolaridade = None  # Associação com Escolaridade (1)
        self.naturalidade = None  # Associação com Cidade (1)

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
        # Delegação
        if self.escolaridade:
            return self.escolaridade.get_nome()
        return "Escolaridade não definida"
        
    def get_nome_estado_naturalidade(self):
        # Delegação encadeada
        if self.naturalidade:
            return self.naturalidade.get_nome_estado()
        return "Estado de naturalidade não definido"

    def get_nome_cidade_naturalidade(self):
        # Delegação
        if self.naturalidade:
            return self.naturalidade.get_nome()
        return "Cidade de naturalidade não definida"

# Professor É UMA Pessoa (Herança)
class Professor(Pessoa):
    def __init__(self, nome):
        super().__init__(nome)
        # Relação 'contratação' (um professor pode dar aula em N cursos)
        self.cursos_lecionados = [] 
        # Relação 'direção' (um professor pode dirigir UMA escola)
        self.escola_dirigida = None
        # Relação 'coordenação' (um professor pode coordenar UM curso)
        self.curso_coordenado = None

    def add_curso_lecionado(self, curso):
        if curso not in self.cursos_lecionados:
            self.cursos_lecionados.append(curso)
            curso.add_professor(self) # Mantém a consistência da relação N:M

    def get_cursos_lecionados(self):
        return self.cursos_lecionados

    def set_escola_dirigida(self, escola):
        self.escola_dirigida = escola
        # Não precisa chamar escola.set_diretor(self) aqui para evitar loop
        
    def get_escola_dirigida(self):
        return self.escola_dirigida

    def set_curso_coordenado(self, curso):
        self.curso_coordenado = curso
        # Não precisa chamar curso.set_coordenador(self) aqui para evitar loop
        
    def get_curso_coordenado(self):
        return self.curso_coordenado

# Aluno É UMA Pessoa (Herança)
class Aluno(Pessoa):
    def __init__(self, nome):
        super().__init__(nome)
        self.curso = None  # Associação com Curso (1)

    def set_curso(self, curso):
        self.curso = curso
        # Não precisa chamar curso.add_aluno(self) aqui para evitar loop

    def get_curso(self):
        return self.curso

class Curso:
    def __init__(self, nome, tipo_ensino):
        self.nome = nome
        self.tipo_ensino = tipo_ensino  # Associação com TipoEnsino (1)
        self.coordenador = None         # Associação com Professor (1) - 'coordenação'
        self.escola = None              # Associação com Escola (1)
        self.alunos = []                # Associação com Aluno (N)
        self.professores = []           # Associação com Professor (N) - 'contratação'

    def get_nome(self):
        return self.nome

    def get_tipo_ensino(self):
        return self.tipo_ensino

    def set_coordenador(self, professor):
        self.coordenador = professor
        if professor.get_curso_coordenado() != self:
            professor.set_curso_coordenado(self) # Relação bidirecional

    def get_coordenador(self):
        return self.coordenador

    def set_escola(self, escola):
        self.escola = escola
        if self not in escola.get_cursos():
             escola.add_curso(self) # Relação bidirecional

    def get_escola(self):
        return self.escola

    def add_aluno(self, aluno):
        if aluno not in self.alunos:
            self.alunos.append(aluno)
            aluno.set_curso(self) # Relação bidirecional
            
    def get_alunos(self):
        return self.alunos
        
    def add_professor(self, professor):
        if professor not in self.professores:
            self.professores.append(professor)
            professor.add_curso_lecionado(self) # Relação bidirecional

    def get_professores(self):
        return self.professores

    def get_nome_coordenador(self):
        if self.coordenador:
            return self.coordenador.get_nome()
        return "Curso sem coordenador"

class Escola:
    def __init__(self, nome, cidade):
        self.nome = nome
        self.cidade = cidade      # Associação com Cidade (1)
        self.diretor = None       # Associação com Professor (1) - 'direção'
        self.cursos = []          # Associação com Curso (N)

    def get_nome(self):
        return self.nome

    def set_diretor(self, professor):
        self.diretor = professor
        if professor.get_escola_dirigida() != self:
            professor.set_escola_dirigida(self) # Relação bidirecional

    def get_diretor(self):
        return self.diretor
        
    def get_nome_diretor(self):
        if self.diretor:
            return self.diretor.get_nome()
        return "Escola sem diretor"

    def add_curso(self, curso):
        if curso not in self.cursos:
            self.cursos.append(curso)
            curso.set_escola(self) # Relação bidirecional
            
    def get_cursos(self):
        return self.cursos

    def get_cidade(self):
        return self.cidade

# --- 2. CRIAÇÃO DOS OBJETOS (CASOS DE TESTE) ---

# Criando Estados
estado_rj = Estado("Rio de Janeiro")
estado_sp = Estado("São Paulo")

# Criando Cidades
cidade_niteroi = Cidade("Niterói", estado_rj)
cidade_rio = Cidade("Rio de Janeiro", estado_rj)
cidade_sp = Cidade("São Paulo", estado_sp)

# Criando Níveis de Escolaridade
ens_medio = Escolaridade("Ensino Médio")
graduacao = Escolaridade("Graduação")
mestrado = Escolaridade("Mestrado")
doutorado = Escolaridade("Doutorado")

# Criando Tipos de Ensino
tipo_superior = TipoEnsino("Ensino Superior")

# Criando Pessoas (Professores e Alunos)
prof_ada = Professor("Ada Lovelace")
prof_ada.set_naturalidade(cidade_sp)
prof_ada.set_escolaridade(doutorado)

prof_alan = Professor("Alan Turing")
prof_alan.set_naturalidade(cidade_rio)
prof_alan.set_escolaridade(doutorado)

aluno_bob = Aluno("Bob")
aluno_bob.set_naturalidade(cidade_niteroi)
aluno_bob.set_escolaridade(ens_medio) # Aluno pode ter escolaridade anterior ao curso

aluna_grace = Aluno("Grace Hopper")
aluna_grace.set_naturalidade(cidade_sp)
aluna_grace.set_escolaridade(graduacao) # Aluna já tem graduação e está fazendo outra

# Criando Escola
escola_tech = Escola("Instituto de Computação", cidade_niteroi)

# Criando Cursos
curso_ads = Curso("Análise e Desenvolvimento de Sistemas", tipo_superior)
curso_si = Curso("Sistemas de Informação", tipo_superior)

# --- ASSOCIANDO OS OBJETOS ---

# 1. Escola contrata Diretor
escola_tech.set_diretor(prof_alan)

# 2. Escola oferece Cursos
escola_tech.add_curso(curso_ads)
escola_tech.add_curso(curso_si)

# 3. Cursos têm Coordenadores
curso_ads.set_coordenador(prof_ada)
# (Vamos deixar o curso_si sem coordenador para testar)

# 4. Alunos se matriculam nos Cursos
curso_ads.add_aluno(aluno_bob)
curso_si.add_aluno(aluna_grace)

# 5. Professores são contratados para Cursos
curso_ads.add_professor(prof_ada) # Ada coordena e dá aula em ADS
curso_si.add_professor(prof_alan) # Alan dirige a escola e dá aula em SI
curso_si.add_professor(prof_ada)  # Ada também dá aula em SI


# --- 3. RESPOSTAS DAS PERGUNTAS ---

print("--- Respostas do Exercício Relâmpago ---")

# a) Qual a escolaridade de um professor? (Ex: Prof. Ada)
print(f"a) Escolaridade da Profa. Ada: {prof_ada.get_nome_escolaridade()}")

# b) Qual a escolaridade do coordenador de um curso? (Ex: Curso ADS)
#     Curso -> Coordenador (Professor) -> Escolaridade
coordenador_ads = curso_ads.get_coordenador()
print(f"b) Escolaridade do Coordenador de ADS (Profa. Ada): {coordenador_ads.get_nome_escolaridade()}")

# c) Qual a escolaridade do diretor de uma escola? (Ex: Escola Tech)
#     Escola -> Diretor (Professor) -> Escolaridade
diretor_escola = escola_tech.get_diretor()
print(f"c) Escolaridade do Diretor da Escola (Prof. Alan): {diretor_escola.get_nome_escolaridade()}")

# d) Qual o estado de naturalidade de um aluno? (Ex: Aluno Bob)
#     Aluno -> Naturalidade (Cidade) -> Estado -> Nome
print(f"d) Estado de naturalidade do Aluno Bob: {aluno_bob.get_nome_estado_naturalidade()}")

# e) Qual a cidade de nascimento de um professor? (Ex: Prof. Alan)
#     Professor -> Naturalidade (Cidade) -> Nome
print(f"e) Cidade de nascimento do Prof. Alan: {prof_alan.get_nome_cidade_naturalidade()}")

# f) Qual o estado em que um aluno estuda? (Ex: Aluna Grace)
#     Aluno -> Curso -> Escola -> Cidade -> Estado -> Nome
estado_escola_grace = aluna_grace.get_curso().get_escola().get_cidade().get_estado().get_nome()
print(f"f) Estado onde a Aluna Grace estuda: {estado_escola_grace}")

# g) Qual o tipo de ensino que um professor foi contratado para lecionar? (Ex: Prof. Ada, no curso ADS)
#     Professor -> Cursos Lecionados [0] -> Tipo de Ensino -> Nome
tipo_ensino_prof_ada = prof_ada.get_cursos_lecionados()[0].get_tipo_ensino().get_nome()
print(f"g) Tipo de ensino que a Profa. Ada leciona: {tipo_ensino_prof_ada}")

# h) Quem é o coordenador do curso de um aluno? (Ex: Aluno Bob)
#     Aluno -> Curso -> Coordenador (Professor) -> Nome
nome_coordenador_bob = aluno_bob.get_curso().get_nome_coordenador()
print(f"h) O coordenador do Aluno Bob é: {nome_coordenador_bob}")

# i) Quem é o diretor de um professor? (Ex: Profa. Ada)
#     Professor -> Cursos Lecionados [0] -> Escola -> Diretor (Professor) -> Nome
diretor_prof_ada = prof_ada.get_cursos_lecionados()[0].get_escola().get_nome_diretor()
print(f"i) O diretor da Profa. Ada é: {diretor_prof_ada}")

# j) Quem é o coordenador de um professor? (Ex: Prof. Alan, que leciona em SI)
#     (Assumindo: "Quem coordena o curso que o Prof. Alan leciona?")
#     Professor -> Cursos Lecionados [0] -> Coordenador (Professor) -> Nome
curso_prof_alan = prof_alan.get_cursos_lecionados()[0] # Ele leciona em SI
nome_coordenador_prof_alan = curso_prof_alan.get_nome_coordenador()
print(f"j) O coordenador do curso do Prof. Alan (SI) é: {nome_coordenador_prof_alan}")