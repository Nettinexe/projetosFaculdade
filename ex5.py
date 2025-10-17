# 5. Classe Produto
class Produto:
    def __init__(self):
        self._nome = ""
        self._preco = 0.0
        self._quantidade_estoque = 0
        self._categoria = ""

    def adicionar_estoque(self, quantidade):
        if quantidade > 0:
            self._quantidade_estoque += quantidade

    def remover_estoque(self, quantidade):
        if 0 < quantidade <= self._quantidade_estoque:
            self._quantidade_estoque -= quantidade

    def aplicar_desconto(self, percentual):
        if 0 < percentual <= 100:
            self._preco -= self._preco * (percentual / 100)