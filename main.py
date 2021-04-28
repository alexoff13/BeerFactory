from enum import Enum


class Color(Enum):
    RED = 1
    BLACK = 2
    RAINBOW = 3


class Beer:
    def __init__(self, name: str, alcohol: float, firm: str, color: Color):
        self.__name = name
        self.__color = color
        self.__alcohol = alcohol if 0.0 < alcohol < 100.0 else 0.0
        self.__firm = firm

    @property
    def name(self):
        return self.__name

    @property
    def color(self):
        return self.__color

    @property
    def alcohol(self):
        return self.__alcohol

    @property
    def firm(self):
        return self.__firm

    @staticmethod
    def create_baltika9():
        return Beer('Baltika9', 50.0, ' OOO "Baltika"', Color.BLACK)

    @staticmethod
    def create_amsterdam():
        return Beer('Amsterdam', 70.0, ' OOO "Baltika"', Color.RED)

    @staticmethod
    def create_essa():
        return Beer('ESSA', 5.0, ' OOO "Baltika"', Color.RAINBOW)

    def __str__(self):
        return f'{self.__name}, color: ' \
               f'{self.__color.name}' \
               f' with {self.__alcohol} % alcohol, made in {self.__firm}'


if __name__ == '__main__':
    beers = list()
    beers.append(Beer.create_amsterdam())
    beers.append(Beer.create_essa())
    beers.append(Beer.create_baltika9())

    print(*beers, sep='\n')
