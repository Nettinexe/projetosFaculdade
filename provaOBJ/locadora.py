class Veiculo:
    def __init__(self):
        self._placa = ""
        self._modelo = ""
        self._estado = "disponivel"
        self._qntdalg = 0
    def set_placa(self,placa):
        self._placa = placa
    def get_placa(self):
        return self._placa
    def set_modelo(self,modelo):
        self._modelo = modelo
    def get_modelo(self):
        return self._modelo
    def set_estado(self,estado):
        self._estado = estado
    def get_estado(self):
        return self._estado
    def set_qntdalg(self,qntdalg):
        self._qntdalg = qntdalg
    def get_qntdalg(self):
        return self._qntdalg
    
    def alugar(self):
        if self._estado == "disponivel":
            self._estado = "alugado"
            self._qntdalg +=1
            return "Veículo alugado com sucesso!"
        else:
            return"Este veículo está alugado!"
    def devolver(self, dias):
        if self._estado != "alugado":
            return "Este carro não foi alugado"
        self._estado = "disponivel"
        atraso = dias - self.prazo()
        if atraso > 0:
            multa = atraso * self.multa_dia()
        else:
            multa = 0
        return f"Veículo devolvido com sucesso! A Multa é de: R${multa:.2f}"

class Automovel(Veiculo):
    def prazo(self):
        return 6
    def multa_dia(self):
        return 50.00
class Onibus(Veiculo):
    def prazo(self):
        return 10
    def multa_dia(self):
        return 200.00
    
a = Automovel()
print(a.alugar())
print(a.devolver(10))
o = Onibus()
print(o.alugar())
print(o.devolver(20))