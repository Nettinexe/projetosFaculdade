class Escolaridade:
    def __init__(self):
        self.nome = ""

    def get_nome(self):
        return self.nome
    
    def set_nome(self,nome):
        self.nome = nome

class Pais:
    def __init__(self, ):
        self.nome = ""

    def get_nome(self):
        return self.nome
    
    def set_nome(self,nome):
        self.nome = nome

class Estado:
    def __init__(self):
        self.nome = ""
        self.pais = None

    def get_nome(self):
        return self.nome
    
    def set_nome(self,nome):
        self.nome = nome
    
    def get_pais(self):
        return self.pais
    
    def set_pais(self, pais):
        self.pais = pais

class Cidade:
    def __init__(self):
        self.nome = ""
        self.estado = None

    def get_nome(self):
        return self.nome
    
    def set_nome(self,nome):
        self.nome = nome
    
    def get_estado(self):
        return self.estado
    
    def set_estado(self, estado):
        self.estado = estado

class Funcionario:
    def __init__(self):
        self.nome = ""
        self.escolaridade = None
        self.alocacao = None
        self.coordenacao = None
    def set_nome(self, nome):
        self.nome = nome
    def get_nome(self):
        return self.nome
    def set_escolaridade(self, escolaridade):
        self.escolaridade = escolaridade
    def get_escolaridade(self):
        return self.escolaridade
    def set_alocacao(self, alocacao):
        self.alocacao = alocacao
    def get_alocacao(self):
        return self.alocacao
    def set_coordenacao(self, coordenacao):
        self.coordenacao = coordenacao
    def get_coordenacao(self):
        return self.coordenacao
    
    def get_nome_pais_alocacao(self):
        if self.alocacao == None:
            return "Funcionário não alocado"
        else:
            empresa = self.alocacao.get_empresa()
            if empresa == None:
                return "Departamento sem empresa"
            else:
                grupo = empresa.get_grupo()
                if grupo == None:
                    return "A empresa não pertence a nenhum grupo"
                else:
                    pais = grupo.get_sede()
                    if pais == None:
                        return "O grupo não tem sede"
                    else:
                        return pais.get_nome()

    def get_nome_estado_coordenacao(self):
        if self.coordenacao == None:
            return "Funcionário não coordena filial"
        else:
            cidade = self.coordenacao.get_cidade()
            if cidade == None:
                return "Filial sem cidade"
            else:
                estado = cidade.get_estado()
                if estado == None:
                    return "Cidade sem estado"
                else:
                    return estado.get_nome()

class Departamento:
    def __init__(self):
        self.nome = ""
        self.empresa = None
        self.chefia = None
    def set_nome(self, nome):
        self.nome = nome
    def get_nome(self):
        return self.nome
    def set_empresa(self, empresa):
        self.empresa = empresa
    def get_empresa(self):
        return self.empresa
    def set_chefia(self, chefia):
        self.chefia = chefia
    def get_chefia(self):
        return self.chefia
    
    def get_nome_escolaridade_chefe(self):
        if self.chefia == None:
            return "Departamento sem chefe"
        else:
            escolaridade = self.chefia.get_escolaridade()
            if escolaridade == None:
                return "Chefe sem escolaridade"
            else:
                return escolaridade.get_nome()
    
class Empresa:
    def __init__(self):
        self.nome = ""
        self.diretor = None
        self.grupo = None
    def set_nome(self, nome):
        self.nome = nome
    def get_nome(self):
        return self.nome
    def set_diretor(self, diretor):
        self.diretor = diretor
    def get_diretor(self):
        return self.diretor
    def set_grupo(self, grupo):
        self.grupo = grupo
    def get_grupo(self):
        return self.grupo
    
class Filial:
    def __init__(self):
        self.nome = ""
        self.cidade = None
        self.empresa = None
    def set_nome(self, nome):
        self.nome = nome
    def get_nome(self):
        return self.nome
    def set_cidade(self, cidade):
        self.cidade = cidade
    def get_cidade(self):
        return self.cidade
    def set_empresa(self, empresa):
        self.empresa = empresa
    def get_empresa(self):
        return self.empresa
    
    def get_nome_diretor_empresa(self):
        if self.empresa == None:
            return "Filial sem empresa"
        else:
            diretor = self.empresa.get_diretor()
            if diretor == None:
                return "Empresa sem diretor"
            else:
                return diretor.get_nome()
    
class Grupo:
    def __init__(self):
        self.nome = ""
        self.presidente = None
        self.sede= None
    def set_nome(self, nome):
        self.nome = nome
    def get_nome(self):
        return self.nome
    def set_presidente(self, presidente):
        self.presidente = presidente
    def get_presidente(self):
        return self.presidente
    def set_sede(self, sede):
        self.sede = sede
    def get_sede(self):
        return self.sede
    
    def get_nome_presidente_escolaridade(self):
        if self.presidente == None:
            return "Grupo sem presidente"
        else:
            escolaridade_do_presidente = self.presidente.get_escolaridade()
            if escolaridade_do_presidente == None:
                return "Presidente sem escolaridade"
            else:
                return escolaridade_do_presidente.get_nome()