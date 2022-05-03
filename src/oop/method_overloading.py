'''
Method Overloading
同一個function，但參數不同，功能不同
python用default
'''


class Cat:

    def __init__(self, name="No-name"):
        self.__name = name

    def shout(self):
        return f"My name is {self.__name}."


def main():
    cat = Cat()
    kelly = Cat(name='Kelly')
    print(cat.shout())
    print(kelly.shout())


if __name__ == "__main__":
    main()
