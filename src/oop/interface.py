'''
Interface
更完全地收像化「抽象類別」
所有方法都未實現

抽象類別」是從子類中發現共通的東西，而泛化出現的
「接口」可以根本不預先知道子類是什麼，而僅僅事先定義行為本身
換句話說，「抽象類別」是類別的抽象化，而「接口」則是行為的抽象化
'''

import abc


class IFLY(abc.ABC):

    @abc.abstractmethod
    def flyTo(self, place):
        pass


class Animal(abc.ABC):

    def __init__(self, name="No-Name"):
        self._name = name
        self._shout_num = 3

    @property
    def shout_num(self):
        return self._shout_num

    @shout_num.setter
    def shout_num(self, num):
        self._shout_num = num

    def shout(self):
        result = ""
        for _ in range(self._shout_num):
            result += f'{self._getShoutSound()}'
        return f"My Name is {self._name}. {result}"

    @abc.abstractmethod
    def _getShoutSound(self):
        pass


class Cat(Animal):

    def _getShoutSound(self):
        return "meow~"


class FlyingCat(Cat, IFLY):
    def flyTo(self, place):
        return f"{self.shout()} I'm going to  fly to {place}."


def main():
    cat = FlyingCat("Kelly")
    print(cat.flyTo("Taiwan"))


if __name__ == '__main__':
    main()
