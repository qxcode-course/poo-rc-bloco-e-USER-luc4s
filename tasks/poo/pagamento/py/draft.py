from abc import ABC, abstractmethod

class Pagamento(ABC):
    def __init__(self, valor: float):
        self.valor = valor
    
    @abstractmethod
    def valor(self):
        pass
    
    @abstractmethod
    def descricao(self):
        pass