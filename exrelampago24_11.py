from datetime import date, datetime

class Pessoa:
    def __init__(self, nome):
        self._nome = nome
    def set_nome(self, nome):
        self._nome = nome
    def get_nome(self):
        return self._nome

class Funcionario(Pessoa):
    def __init__(self, nome, cargo):
        super().__init__(nome)
        self._cargo = cargo
        self._dependente = []
        self._ocorrencia = []

    def set_cargo(self, cargo):
        self._cargo = cargo
    def get_cargo(self):
        return self._cargo
    
    def adicionar_dependente(self, dependente):
        self._dependente.append(dependente)
    
    def adicionar_ocorrencia(self, ocorrencia):
        self._ocorrencia.append(ocorrencia)

    def calcularSalarioLiquido(self, mes, ano):
        salario_final = self.get_cargo().get_salarioBruto()

        for ocorrencia in self._ocorrencia:
            data = ocorrencia.get_dataOcorrencia()
            if data.month == mes and data.year == ano:
                salario_final += ocorrencia.get_valorAcrescimo()
                salario_final -= ocorrencia.get_valorDesconto()

        for dependente in self._dependente:
            nascimento = dependente.get_dataNascimento()
            idade = ano - nascimento.year
            if idade < 18:
                salario_final += 100.0
        
        return salario_final

    def exibirDependentes(self):
        hoje = date.today()
        dias_semana = ['Segunda-feira', 'Terça-feira', 'Quarta-feira', 'Quinta-feira', 'Sexta-feira', 'Sábado', 'Domingo']

        for dependente in self._dependente:
            nome = dependente.get_nome()
            nasc = dependente.get_dataNascimento()

            try:
                proximo_niver = date(hoje.year, nasc.month, nasc.day)
            except ValueError:
                proximo_niver = date(hoje.year, nasc.month + 1, 1)

            if proximo_niver < hoje:
                try:
                    proximo_niver = date(hoje.year + 1, nasc.month, nasc.day)
                except ValueError:
                    proximo_niver = date(hoje.year + 1, nasc.month + 1, 1)

            dias_restantes = (proximo_niver - hoje).days
            nome_dia = dias_semana[proximo_niver.weekday()]

            print(f"Nome: {nome} | Data de Nascimento: {nasc.strftime('%d/%m/%Y')}")
            print(f"Próximo aniversário: {proximo_niver.strftime('%d/%m/%Y')} | Dias restantes: {dias_restantes}")
            print(f"Dia da semana do próximo aniversário: {nome_dia}")
            print("-" * 30)

class Cargo:
    def __init__(self, salarioBruto):
        self._salarioBruto = salarioBruto
    def set_salarioBruto(self, salarioBruto):
        self._salarioBruto = salarioBruto
    def get_salarioBruto(self):
        return self._salarioBruto

class Ocorrencia:
    def __init__(self, dataOcorrencia, valorAcrescimo, valorDesconto, descricaoOcorrencia):
        self._dataOcorrencia = dataOcorrencia
        self._valorAcrescimo = valorAcrescimo
        self._valorDesconto = valorDesconto
        self._descricaoOcorrencia = descricaoOcorrencia
    def set_dataOcorrencia(self, dataOcorrencia):
        self._dataOcorrencia = dataOcorrencia
    def get_dataOcorrencia(self):
        return self._dataOcorrencia
    def set_valorAcrescimo(self, valorAcrescimo):
        self._valorAcrescimo = valorAcrescimo
    def get_valorAcrescimo(self):
        return self._valorAcrescimo
    def set_valorDesconto(self, valorDesconto):
        self._valorDesconto = valorDesconto
    def get_valorDesconto(self):
        return self._valorDesconto
    def set_descricaoOcorrencia(self, descricaoOcorrencia):
        self._descricaoOcorrencia = descricaoOcorrencia
    def get_descricaoOcorrencia(self):
        return self._descricaoOcorrencia

class Dependente(Pessoa):
    def __init__(self, dataNascimento, nome):
        super().__init__(nome)
        self._dataNascimento = dataNascimento
    def set_dataNascimento(self, dataNascimento):
        self._dataNascimento = dataNascimento
    def get_dataNascimento(self):
        return self._dataNascimento