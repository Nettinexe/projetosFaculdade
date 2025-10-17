# 4. Classe Pessoa
class Pessoa:
    def __init__(self):
        self._nome = ""
        self._idade = 0
        self._altura = 0.0
        self._peso = 0.0

    def envelhecer(self):
        self._idade += 1

    def crescer(self, centimetros):
        if self._idade < 21:
            self._altura += centimetros

    def ganhar_peso(self, quilos):
        self._peso += quilos

    def perder_peso(self, quilos):
        # regra: não deixa ficar negativo; se pedir demais, zera
        if quilos > 0:
            self._peso = max(0.0, self._peso - quilos)
