class Obra:
    def __init__(self):
        self._titulo = ""
        self._autor = ""
        self._ano = 0
        self._editora = ""
        self._estado = "disponivel"
        self._qntdemp = 0
    def set_titulo(self,titulo):
        self._titulo = titulo
    def get_titulo(self):
        return self._titulo
    def set_autor(self,autor):
        self._autor = autor
    def get_autor(self):
        return self._autor
    def set_ano(self,ano):
        self._ano= ano
    def get_ano(self):
        return self._ano
    def set_editora(self,editora):
        self._editora = editora
    def get_editora(self):
        return self._editora
    def set_estado(self,estado):
        self._estado = estado
    def get_estado(self):
        return self._estado
    def set_qntdemp(self,qntdemp):
        self._qntdemp = qntdemp
    def get_qntdemp(self):
        return self._qntdemp
    
    def emprestar(self):
        if self._estado == "disponivel":
            self._qntdemp += 1
            self._estado = "emprestado"
            return "Livro emprestado com sucesso!"
        else:
            return "Este livro não está disponível no momento"
    def devolver(self, dias):
        if self._estado != "emprestado":
            return "Este livro não foi emprestado"
        self._estado = "disponivel"
        atraso = dias - self.prazo()
        if atraso > 0:
            multa = atraso * self.multa_dia()
        else:
            multa = 0
        return f"Livro devolvido! Multa: R${multa:.2f}"

        
class Livro(Obra):
    def prazo(self):
        return 6
    def multa_dia(self):
        return 5.0
class Periodico(Obra):
    def prazo(self):
        return 10
    def multa_dia(self):
        return 2.0
l = Livro()
print(l.emprestar())   # → Livro emprestado com sucesso!
print(l.devolver(8))   # → Livro devolvido! Multa: R$10.00

p = Periodico()
print(p.emprestar())   # → Livro emprestado com sucesso!
print(p.devolver(12))  # → Livro devolvido! Multa: R$4.00
