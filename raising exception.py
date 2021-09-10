class CoffeeCup:
    def __init__(self, temperature):
        self.__temperature = temperature

    def drink_coffee(self):
        if self.__temperature > 85:
            print('coffee too hot')
            raise Exception
        elif self.__temperature < 65:
            print('coffee too cold')
            raise ValueError ('coffee too cold')     # any exception found in builtins import found in console
        else:
            print('coffee ok to drink')


cup = CoffeeCup(50)
cup.drink_coffee()
