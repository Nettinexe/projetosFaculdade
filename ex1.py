# Lista de Exercícios de POO - Completa

# 1. Classe Carro
class Carro:
    def __init__(self):
        self._marca = ""
        self._modelo = ""
        self._ano = 0
        self._velocidade_atual = 0
        self._ligado = False

    def set_marca(self, marca):
        self._marca = marca

    def get_marca(self):
        return self._marca

    def set_modelo(self, modelo):
        self._modelo = modelo

    def get_modelo(self):
        return self._modelo

    def set_ano(self, ano):
        if ano >= 0:
            self._ano = ano

    def get_ano(self):
        return self._ano

    def set_velocidade_atual(self, velocidade_atual):
        if velocidade_atual >= 0:
            self._velocidade_atual = velocidade_atual

    def get_velocidade_atual(self):
        return self._velocidade_atual

    def set_ligado(self, ligado):
        self._ligado = ligado

    def get_ligado(self):
        return self._ligado

    def acelerar(self, quantidade):
        if self._ligado:
            if quantidade >= 0:
                self._velocidade_atual += quantidade

    def frear(self, quantidade):
        if self._ligado:
            if quantidade >= 0:
                self._velocidade_atual -= quantidade
                if self._velocidade_atual < 0:
                    self._velocidade_atual = 0

    def ligar(self):
        if not self._ligado:
            self._ligado = True

    def desligar(self):
        if self._ligado:
            if self._velocidade_atual == 0:
                self._ligado = False
                self._velocidade_atual = 0
