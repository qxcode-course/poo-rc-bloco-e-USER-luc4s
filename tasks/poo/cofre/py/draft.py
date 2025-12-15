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
        pass
    
from enum import Enum

class Coin(Enum):
    m10 = ("M10", 0.10, 1)
    m25 = ("M25", 0.25, 1)
    m50 = ("M50", 0.50, 1)
    m100 = ("M100", 1.00, 1)

    def __init__(self, label: str, value: float, volume: int):
        self.label = label
        self.value = value
        self.volume = volume

    def get.Label(self) -> str:
        return self.label
    
    def getValue(self) -> float:
        return self.value
    
    def getVolume(self) -> int:
        return self.volume

    def __str__(self) -> str:
        return self.label
