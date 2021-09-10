class CoffeeTooHotException(Exception):
    def __init__(self, msg):
        super().__init__(msg)


class CoffeeTooColdException(Exception):
    def __init__(self, msg):
        super().__init__(msg)


class CoffeeCup:
    def __init__(self, temperature):
        self.__temperature = temperature

    def drink_coffee(self):
        if self.__temperature > 85:
            print('coffee too hot')
            raise CoffeeTooHotException('coffee temp.:' + str(self.__temperature))
        elif self.__temperature < 65:
            print('coffee too cold')
            raise CoffeeTooColdException('coffee temp.:' + str(self.__temperature))    # any exception found in builtins import found in console
        else:
            print('coffee ok to drink')


cup = CoffeeCup(100)
cup.drink_coffee()
