from abc import ABC, abstractmethod

class Pagamento(ABC):
    def __init__(self, valor: float, descricao: str):
        self.valor = valor
        self.descricao = descricao
    
    @abstractmethod
    def validar_valor(self) -> None:
        if self.valor  <= 0:
            raise ValueErro("valor negativo")
    
    def resumo(self):
        return f"Pagamento de R$ <valor>: <descricao>"
    
    @abstractmethod
    def processar(self):
        pass

class Pix(Pagamento):
    def __init__(self, valor: float, descricao: str, chave: str, banco: str):
        super.__init__(valor, descricao)
        self.chave = chave
        self.banco = banco
    
    def realizar_pagamento(self):
        return f"Pagando pix produto{self.descricao} para {self.chave} do banco {self.banco} no valor {self.valor}"

class Cartao(Pagamento):
    def __init__(self,numero: str, nome: str valor: float, descricao: str, limite_disponivel: float):
        super().__init__(valor, descricao)
        self.numero = numero
        self.nome = nome
        self.limite_disponivel = limite_disponivel

    def realizar_pagamento(self):
        if self.valor > self.limite_disponivel:
            raise Exception(f"Erro: Limite insuficiente")
        else:
            limite_disponivel -= self.valor
            return "Pagamento concluido"


    