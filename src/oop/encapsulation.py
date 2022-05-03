'''
Encapsulation
'''


class Cat:

    def __init__(self, name='No-Name'):
        self.__name = name
        self.__shout_num = 3

    @property
    def shout_num(self):
        return self.__shout_num

    @shout_num.setter
    def shout_num(self, num):
        if num < 0:
            raise ValueError()
        self.__shout_num = num

    def shout(self):
        result = ""
        for _ in range(self.__shout_num):
            result += "meow~"
        return f"My name is {self.__name}. {result}"


def main():
    cat = Cat("May")
    cat.shout_num = 5
    print(cat.shout())


if __name__ == '__main__':
    main()
