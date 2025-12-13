from abc import ABC, abstractmethod

class Veiculo(ABC):
    def __init__(self, id: str, tipo: str):
        self.id = id
        self.tipo = tipo
        self.horaE = 0

    def setEntrada(self, horaE: int) -> None:
        self.horaE = horaE

    def getEntrada(self) -> float:
        return self.horaE
    def getTipo(self) -> str:
        return self.tipo
    def getId(self) -> str:
        return self.id
    
    @abstractmethod
    def calcularValor(self, horaS: int) -> float:
        pass
    
    def __str__(self) -> str:
        return f"{self.tipo}:{self.id} entrada={self.horaE}"

class Bike(Veiculo):
    def __init__(self, id: str):
        super().__init__(id, "Bike")

    def calcularValor(self, horaS: int) -> float:
        return 3.0

class Moto(Veiculo):
    def __init__(self, id: str):
        super().__init__(id, "Moto")

    def calcularValor(self, horaS: int) -> float:
        tempo = horaS - self.horaE
        return tempo / 20

class Carro(Veiculo):
    def __init__(self, id: str):
        super().__init__(id, "Carro")

    def calcularValor(self, horaS: int) -> float:
        tempo = horaS - self.horaE
        valor = tempo / 10
        return max(5.0, valor)

class Estacionamento:
    def __init__(self, horaA: int):
        self.horaA = horaA
        self.veiculos: list[Veiculo] = []

    def procurarVeiculo(self, id: str) -> int:
        for i, v in enumerate(self.veiculos):
            if v.getId() == id:
                return i
        return -1
    def estacionar(self, veiculo: Veiculo) -> None:

    def pagar(self, id: str) -> None:

    def sair(self, id: str) -> None:

    def passarTempo(self, tempo: int) -> None:

    def __str__(self) -> str:
        return f"" 
