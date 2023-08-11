class HotBeverage:
    def __init__(self) -> None:
        self.preco = 0.30
        self.nome = "hot beverage"
    def description(self):
        return "Just some hot water in a cup."
    def __str__(self) -> str:
        return f'nome: {self.nome}\npreco: {self.preco:.2f}\ndescricao: {self.description()}\n'

class Coffee(HotBeverage):
    def __init__(self) -> None:
        super().__init__()
        self.preco = 0.40
        self.nome = "coffee"
    def description(self):
        return "A coffee, to stay awake."

class Tea(HotBeverage):
    def __init__(self) -> None:
        super().__init__()
        self.preco = 0.30
        self.nome = "tea"
    def description(self):
        return super().description()

class Chocolate(HotBeverage):
    def __init__(self) -> None:
        super().__init__()
        self.preco = 0.50
        self.nome = "chocolate"
    def description(self):
        return "Chocolate, sweet chocolate..."
    
class Cappuccino(HotBeverage):
    def __init__(self) -> None:
        super().__init__()
        self.preco = 0.45
        self.nome = "cappuccino"
    def description(self):
        return "Un po’ di Italia nella sua tazza!"

# def teste():
#     hot_beverage = HotBeverage()
#     coffe = Coffee()
#     tea = Tea()
#     chocolate = Chocolate()
#     cappuccino = Cappuccino()

#     print(hot_beverage)
#     print(coffe)
#     print(tea)
#     print(chocolate)
#     print(cappuccino)

# if __name__ == '__main__':
#     teste()