class Pessoa:
    def __init__(self, nome):
        self.__nome = nome
        
    def get_nome(self):
        return self.__nome
    
class Cliente(Pessoa):
    def __init__(self, nome, cpf):
        super().__init__(nome)
        self.__cpf = cpf
        
    def get_cpf(self):
        return self.__cpf
        
class Fornecedor(Pessoa):
    def __init__(self, nome, cnpj):
        super().__init__(nome)
        self.__cnpj = cnpj
        
    def get_cnpj(self):
        return self.__cnpj

class Transacao:
    def __init__(self, dataTransacao, produto, qtde):
        self.__dataTransacao = dataTransacao
        self.__qtde = qtde
        
    def get_dataTransacao(self):
        return self.__dataTransacao
        
    def get_qtde(self):
        return self.__qtde

class Compra(Transacao):
    def __init__(self, dataCompra, fornecedor, qtdeCompra, precoUnit):
        super().__init__(dataCompra, None, qtdeCompra) 
        self.__fornecedor = fornecedor
        self.__precoUnit = precoUnit
    
    def get_fornecedor(self):
        return self.__fornecedor
    
    def get_precoUnit(self):
        return self.__precoUnit

class Venda(Transacao):
    def __init__(self, dataVenda, cliente, produto, qtdeVendida):
        super().__init__(dataVenda, produto, qtdeVendida)
        self.__cliente = cliente
    
    def get_cliente(self):
        return self.__cliente

class Produto:
    def __init__(self, nome, qtdeEstoque, precoUnit, estoqueMinimo, estoqueMaximo):
        self.__nome = nome
        self.__qtdeEstoque = qtdeEstoque
        self.__precoUnit = precoUnit
        self.__estoqueMinimo = estoqueMinimo
        self.__estoqueMaximo = estoqueMaximo
        self.__historico = []

    def get_nome(self):
        return self.__nome
        
    def get_qtdeEstoque(self):
        return self.__qtdeEstoque

    def get_precoUnit(self):
        return self.__precoUnit

    def get_estoqueMinimo(self):
        return self.__estoqueMinimo
        
    def get_estoqueMaximo(self):
        return self.__estoqueMaximo
        
    def debitarEstoque(self, quantidade):
        if quantidade > 0:
            self.__qtdeEstoque -= quantidade 
            
    def creditarEstoque(self, quantidade):
        if quantidade > 0:
            self.__qtdeEstoque += quantidade

    def verificarEstoqueBaixo(self):
        return self.__qtdeEstoque < self.__estoqueMinimo 
        
    def verificarEstoqueInsuficiente(self, quantidade):
        return quantidade > self.__qtdeEstoque
        
    def verificarEstoqueExcedente(self, quantidade):
        return (quantidade + self.__qtdeEstoque) > self.__estoqueMaximo

    def registrarHistorico(self, transacao):
        self.__historico.append(transacao)

    def exibirHistorico(self):
        for item in self.__historico:
            print(item)
            
    def calcularValorVenda(self, quantidade):
        return self.__precoUnit * quantidade
        
    def vender(self, dataVenda, cliente, qtdeVendida):
        if self.verificarEstoqueInsuficiente(qtdeVendida):
            print(f"Estoque insuficiente para vender {qtdeVendida} unidades de {self.get_nome()}.")
            return False
        
        valor_venda = self.calcularValorVenda(qtdeVendida)
        
        print(f"Valor venda = {valor_venda}") 
        
        self.debitarEstoque(qtdeVendida)
        
        registro_venda = Venda(dataVenda, cliente, self, qtdeVendida)
        self.registrarHistorico(registro_venda)

        if self.verificarEstoqueBaixo():
            print("Estoque baixo")
        
        print(f"Venda do produto {self.get_nome()}")
        return True
        
    def comprar(self, dataCompra, fornecedor, qtdeCompra, precoUnit):
        if self.verificarEstoqueExcedente(qtdeCompra):
            print(f"Estoque excedente")
            return False
        
        self.creditarEstoque(qtdeCompra)
        
        registro_compra = Compra(dataCompra, fornecedor, qtdeCompra, precoUnit)
        self.registrarHistorico(registro_compra)
        
        print(f"Compra do produto {self.get_nome()}")
        return True