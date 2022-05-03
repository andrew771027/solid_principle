'''
多型
Polymorphism

「多型」的涵義是指「子類可以以父類的身分出現」
子類別可以執行父類別擁有的方法
'''

import abc


class Animal(abc.ABC):
    def __init__(self, name='No-Name'):
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
            result += self._getShoutSound()
        return f"My name is {self._name}. {result}"

    @abc.abstractmethod
    def _getShoutSound(self):
        pass


class Cat(Animal):

    def _getShoutSound(self):
        return "meow~"


class Dog(Animal):

    def _getShoutSound(self):
        return "woof~"


def main():
    arrayAnimal = []
    arrayAnimal.append(Cat("Kelly"))
    arrayAnimal.append(Dog("Lucky"))
    arrayAnimal.append(Cat("Mini"))

    for animal in arrayAnimal:
        if not isinstance(animal, Animal):
            raise TypeError
        print(animal.shout())


if __name__ == '__main__':
    main()
