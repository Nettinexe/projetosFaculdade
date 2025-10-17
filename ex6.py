# 6. Classe Funcionario
class Funcionario:
    def __init__(self):
        self._nome = ""
        self._cargo = ""
        self._salario = 0.0
        self._departamento = ""

    def receber_aumento(self, percentual):
        if percentual > 0:
            self._salario += self._salario * (percentual / 100)

    def mudar_departamento(self, novo_departamento):
        self._departamento = novo_departamento

    def exibir_dados(self):
        print(f"Nome: {self._nome}")
        print(f"Cargo: {self._cargo}")
        print(f"Salário: {self._salario}")
        print(f"Departamento: {self._departamento}")