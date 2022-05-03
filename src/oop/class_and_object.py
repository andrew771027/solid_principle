'''
Class and Object
'''


class Cat:

    def __init__(self, name):
        self.__name = name

    def shout(self):
        return f"My name is {self.__name}."


def main():
    cat = Cat("Kelly")
    print(cat.shout())


if __name__ == "__main__":
    main()
