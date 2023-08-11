#!/usr/bin/python3
import random
from beverages import HotBeverage, Coffee, Tea, Chocolate, Cappuccino

class CoffeeMachine:
    def __init__(self) -> None:
        self.broken_count = 10

    class EmptyCup(HotBeverage):
        def __init__(self) -> None:
            self.preco = 0.90
            self.nome = "empty cup"
        def description(self):
            return "An empty cup?! Gimme my money back!"
    class BrokenMachineException(Exception):
        def __init__(self) -> None:
            super().__init__("This coffee machine has to be repaired.\n")

    def reparo(self) -> None:
        self.broken_count = 10

    def servir(self, bebida):
        if self.broken_count <= 0:
            raise CoffeeMachine.BrokenMachineException()
        
        self.broken_count -= 1
        if random.randint(0, 5) == 0:
            return CoffeeMachine.EmptyCup()
        return bebida()
    
def test():
    coffe_machine = CoffeeMachine()
    for _ in range(40):
        try:
            print(coffe_machine.servir(random.choice([Coffee, Tea, Chocolate, Cappuccino])))
        except CoffeeMachine.BrokenMachineException as e:
            print(e)
            coffe_machine.reparo()
        
if __name__ == '__main__':
    test()