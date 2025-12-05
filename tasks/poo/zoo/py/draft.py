from abc import ABC, abstractmethod

class Animal(ABC):
    def __init__(self, nome: str):
        self.nome = nome
    
    def apresentar_nome(self):
        print(f"Eu sou um(a) {self.nome}")

    @abstractmethod
    def fazer_som(self):
        pass

    @abstractmethod
    def mover(self):
        pass

class Leao(Animal):
    def __init__(self, nome: str):
        super().__init__(nome)

    def fazer_som(self):
        print("Rããããwwwrr!")
    
    def mover(self):
        print(f"O leão está andando")

class Elefante(Animal):
    def __init__(self, nome: str):
        super().__init__(nome)
    
    def fazer_som(self):
        print("Truuuuuu!")
    
    def mover(self):
        print(f"O elefante está andando")

class Cobra(Animal):
    def __init__(self, nome: str):
        super().__init__(nome)
    
    def fazer_som(self):
        print("Ssssss")
    
    def mover(self):
        print(f"A cobra está andando")

def apresentar(animal: Animal):
    animal.apresentar_nome()
    animal.fazer_som()
    animal.mover()
    print(f"Tipo: {type(animal).__name__}")
    print("-" * 30)
    
animais = [
    Leao("Leão"),
    Elefante("Elefante"),
    Cobra("Cobra")
]

for a in animais:
    apresentar(a)