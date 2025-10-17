# 2. Classe ContaBancaria
class ContaBancaria:
    def __init__(self):
        self._titular = ""
        self._numero_conta = ""
        self._saldo = 0.0

    def set_titular(self, titular):
        self._titular = titular

    def get_titular(self):
        return self._titular

    def set_numero_conta(self, numero):
        self._numero_conta = numero

    def get_numero_conta(self):
        return self._numero_conta

    def get_saldo(self):
        return self._saldo

    def depositar(self, valor):
        if valor > 0:
            self._saldo += valor

    def sacar(self, valor):
        if valor > 0 and valor <= self._saldo:
            self._saldo -= valor