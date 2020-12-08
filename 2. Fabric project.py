from abc import ABC, abstractmethod


class Clothes(ABC):

    @abstractmethod
    def calc_fabric(self):
        pass


class Coat(Clothes, ABC):
    def __init__(self, v, name):
        self.v = v
        self.name = name

    @property
    def calc_fabric(self):
        return self.v / 6.5 + 0.5


class Suit(Clothes, ABC):
    def __init__(self, h, name):
        self.h = h
        self.name = name

    @property
    def calc_fabric(self):
        return 2 * self.h + 0.3


coat_1 = Coat(46, 'Буревестник')
suit_1 = Suit(1.78, 'Джокер')
print(round(coat_1.calc_fabric + suit_1.calc_fabric, 4))
