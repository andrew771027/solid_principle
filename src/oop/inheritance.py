'''
Inheritance

子類別繼承父類別

private 不可被繼承 不可被外部使用
protected 可被繼承 不可被外部使用
public  可被繼承 可被外部使用
'''


class Animal:

    def __init__(self, name="No-name"):
        self._name = name
        self._shout_num = 3

    @property
    def shout_num(self):
        return self._shout_num

    @shout_num.setter
    def shout_num(self, num):
        if num < 0:
            raise ValueError()
        self._shout_num = 3


class Cat(Animal):

    def __init__(self, name="No-name"):
        super().__init__(name)

    def shout(self):
        result = ""
        for _ in range(self._shout_num):
            result += "meow~"
        return f"My name is {self._name}. {result}"


class Dog(Animal):
    def shout(self):
        result = ""
        for _ in range(self._shout_num):
            result += "woof~"
        return f"My name is {self._name}. {result}"


def main():
    cat = Cat()
    dog = Dog()

    print(cat.shout())
    print(dog.shout())


if __name__ == '__main__':
    main()
