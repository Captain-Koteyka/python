from abc import ABC, abstractmethod


class ClothesAbstract(ABC):
    @property
    @abstractmethod
    def name(self) -> str:
        pass


class Coat(ClothesAbstract):
    def __init__(self, size):
        self.__name = 'coat'
        self.size = size

    @property
    def name(self) -> str:
        return self.__name

    def tissue_consumption(self):
        return self.size / 6.5 + 0.5


class Suit(ClothesAbstract):
    def __init__(self, height):
        self.__name = 'suit'
        self.height = height

    @property
    def name(self) -> str:
        return self.__name

    def tissue_consumption(self):
        return 2 * self.height + 0.3


def tissue_consumption_full(coat, suit):
    return coat.tissue_consumption() + suit.tissue_consumption()


coat = Coat(46)
print(coat.name)
print('{:.2f}'.format(coat.tissue_consumption()))
suit = Suit(170)
print(suit.name)
print('{:.2f}'.format(suit.tissue_consumption()))
print('{:.2f}'.format(tissue_consumption_full(coat, suit)))
