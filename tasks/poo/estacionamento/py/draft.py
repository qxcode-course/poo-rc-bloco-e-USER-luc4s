from abc import ABC, abstractmethod

class Veiculo(ABC):
    def __init__(self, id: str, tipo: str):
        self.id = id
        self.tipo = tipo
        self.horaE = 0

    def setEntrada(self, horaE: int) -> None:
        self.horaE = horaE

    def getEntrada(self) -> int:
        return self.horaE
    def getTipo(self) -> str:
        return self.tipo
    def getId(self) -> str:
        return self.id
    
    @abstractmethod
    def calcularValor(self, horaS: int) -> float:
        pass
    
    def __str__(self) -> str:
        return f"______{self.tipo} : _____{self.id} : {self.horaE}"

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
        veiculo.setEntrada(self.horaA)
        self.veiculos.append(veiculo)

    def pagar(self, id: str) -> None:
        idx = self.procurarVeiculo(id)
        if idx == -1:
            print("Veiculo nao encontrado")
            return
        veiculo = self.veiculos[idx]
        valor = veiculo.calcularValor(self.horaA)
        print(
             f"{veiculo.getTipo()} chegou {veiculo.getEntrada()} "
            f"saiu {self.horaA}. Pagar R$ {valor:.2f}"
        )

    def sair(self, id: str) -> None:
        idx = self.procurarVeiculo(id)
        if idx == -1:
            print("Veículo não encontrado")
            return
        veiculo = self.veiculos[idx]
        valor = veiculo.calcularValor(self.horaA)
        print(
            f"{veiculo.getTipo()} chegou {veiculo.getEntrada()} "
            f"saiu {self.horaA}. Pagar R$ {valor:.2f}"
        )
        self.veiculos.pop(idx)

    def passarTempo(self, tempo: int) -> None:
        self.horaA += tempo

    def __str__(self) -> str:
        resultado = ""
        for v in self.veiculos:
            resultado += str(v) + "\n"
        resultado += f"Hora atual: {self.horaA}"
        return resultado

def main():
    est = Estacionamento(0)

    while True:
        try:
            line = input().strip()
        except  EOFError:
            break
        
        if line == "":
            continue
        
        if line == "$end":
            break
        
        partes = line.split()
        comando = partes[0]
        
        if comando == "$show":
            print(est)
        
        elif comando == "$tempo":
            est.passarTempo(int(partes[1]))
        
        elif comando == "$estacionar":
            tipo  = partes[1].lower()
            vid = partes[2]

            if tipo == "bike":
                v = Bike(vid)
            elif tipo == "moto":
                v = Moto(vid)
            elif tipo == "carro":
                v = Carro(vid)
            else:
                continue

            est.estacionar(v)
        
        elif comando == "$pagar":
            est.pagar(partes[1])

if __name__ == "__main__":
    main()
