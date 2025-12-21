from abc import ABC, abstractmethod

class Valuable(ABC):
    @abstractmethod
    def getLabel(self) -> str:
        pass

    @abstractmethod
    def getValue(self) -> float:
        pass
    
    @abstractmethod
    def getVolume(self) -> int:
        pass

    def __str__(self) -> str:
        return f"{self.getLabel()} (R$ {self.getValue():.2f})"
    
from enum import Enum

class Coin(Enum):
    m10 = ("M10", 0.10, 1)
    m25 = ("M25", 0.25, 1)
    m50 = ("M50", 0.50, 1)
    m100 = ("M100", 1.00, 1)

    def __init__(self, label: str, value: float, volume: int):
        self.label = label
        self._value_ = value
        self.volume = volume

    def getLabel(self) -> str:
        return self.label
    
    def getValue(self) -> float:
        return self._value_
    
    def getVolume(self) -> int:
        return self.volume

    def __str__(self) -> str:
        return self.label

class Item(Valuable):
    def __init__(self, label: str, value: float, volume: int):
        self.label = label
        self.value = value
        self.volume = volume

    def getLabel(self) -> str:
        return self.label
    
    def getValue(self) -> float:
        return self.value

    def getVolume(self) -> int:
        return self.volume

    def setLabel(self, label: str) -> None:
        self.label = label
    def setValue(self, value: float) -> None:
        self.value = value
    def setVolume(self, volume: int) -> None:
        self.volume = volume

    def __str__(self) -> str:
        return f"{self.label} (R$ {self.value:.2f})"

class Pig:
    def __init__(self, volumeMax: int):
        self.volumeMax = volumeMax
        self.broken = False
        self.valuables: list[Valuable] = []

    def addValuable(self, valuable: Valuable) -> bool:
        if self.broken:
            return False
        if self.getVolume() + valuable.getVolume() > self.volumeMax:
            return False

        self.valuables.append(valuable)
        return True
    def breakPig(self) -> bool:
        if self.broken:
            return False
        self.broken = True
        return True
        
    def getCoins(self) -> list[Coin]:
        return [v for v in self.valuables if isinstance(v, Coin)]

    def getItems(self) -> list[Item]:
        return [v for v in self.valuables if isinstance(v, Item)]
        
    def calcValue(self) -> float:
        return sum(v.getValue() for v in self.valuables)
        
    def getVolume(self) -> int:
        return sum (v.getVolume() for v in self.valuables)
        
    def getVolumeMax(self) -> int:
        return self.volumeMax
        
    def isBroken(self) -> bool:
        return self.broken
        
    def __str__(self) -> str:
        estado = "broken" if self.broken else "intact"
        itens = [str(v) for v in self.valuables]
        return f"{itens} : {self.calcValue():.2f}$ : {self.getVolume()}/{self.volumeMax} : {estado}"

def main():
    pig = None
    while True:
        try:
            line = input().strip()
        except EOFError:
            break
        
        if line == "":
            continue
        parts = line.split()
        cmd = parts[0]

        if cmd == "end":
            break

        elif cmd == "$show":
            volume = int(parts[1])
            pig = Pig(volume)

        elif cmd == "$show":
            print(pig)

        elif cmd == "$addCoin":
            value = parts[1]

            if pig.isBroken():
                print("fail: the pig is broken")
                continue

            coin_map = {
                "10": Coin.m10,
                "25": Coin.m25,
                "50": Coin.m50,
                "100": Coin.m100
            }

            coin = coin_map[value]

            if not pig.addValuable(coin):
                print("fail: the pig is full")

        elif cmd == "$addItem":
            if pig.isBroken():
                print("fail: the pig is broken")
                continue

            label = parts[1]
            value = float(parts[2])
            volume = int(parts[3])
            item = Item(label, value, volume)

            if not pig.addValuable(item):
                print("fail: the pig is full")

        elif cmd == "$break":
            pig.breakPig()

        elif cmd == "$extractItems":
            if not pig.isBroken():
                print("fail: you must break the pig first")
                continue

            items = pig.extractItems()
            print([f"{i.getLabel()}:{i.getValue():.2f}:{i.getVolume()}" for i in items])

        elif cmd == "$extractCoins":
            if not pig.isBroken():
                print("fail: you must break the pig first")
                continue

            coins = pig.extractCoins()
            print([f"{c.getLabel()}:{c.getValue():.2f}:{c.getVolume()}" for c in coins])