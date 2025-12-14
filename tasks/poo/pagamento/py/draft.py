from abc import ABC, abstractmethod

class Pagamento(ABC):
    def __init__(self, valor: float, descricao: str):
        self.valor = valor
        self.descricao = descricao
     
    def resumo(self):
        print(f"Pagamento de R$ {self.valor}: {self.descricao}")

    def validar_valor(self) -> None:
        if self.valor <= 0:
            raise ValueError("Valor invalido")
    
    @abstractmethod
    def realizar_pagamento(self):
        pass
 
class Pix(Pagamento):
    def __init__(self, valor: float, descricao: str, chave: str, banco: str):
        super().__init__(valor, descricao)
        self.chave = chave
        self.banco = banco
    
    def realizar_pagamento(self):
        print(f"Pix enviado via banco {self.banco}, usando chave {self.chave}.")

class Cartao(Pagamento):
    def __init__(self,numero: str, nome: str, valor: float, descricao: str, limite_disponivel: float):
        super().__init__(valor, descricao)
        self.numero = numero
        self.nome = nome
        self.limite_disponivel = limite_disponivel

    def realizar_pagamento(self):
        if self.valor > self.limite_disponivel:
            print("Erro: Limite insuficiente")
        else:
            self.limite_disponivel -= self.valor
            print("Pagamento concluido")

class Boleto(Pagamento):
    def __init__(self, valor, descricao, codigo_barras, vencimento):
        super().__init__(valor, descricao)
        self.codigo_barras = codigo_barras
        self.vencimento = vencimento

    def realizar_pagamento(self):
        print("Boleto gerado. Aguardando pagamento...")

def realizar_pagamento(pagamento: Pagamento):
    pagamento.validar_valor()
    print(pagamento.resumo())
    pagamento.realizar_pagamento()


    