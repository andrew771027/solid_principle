'''
抽象類別
Abstract Class, Abstract Method
Abstract Class 不能被實例化
在子類別實現
'''

import abc


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


class Dog(Animal):

    def _getShoutSound(self):
        return "Woof~"


def main():

    cat = Cat("kelly")
    dog = Dog("Lucky")

    print(cat.shout())
    print(dog.shout())


if __name__ == '__main__':
    main()
