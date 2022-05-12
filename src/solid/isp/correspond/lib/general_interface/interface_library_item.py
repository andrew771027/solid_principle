import abc
from datetime import datetime


class LibraryItemInterface(abc.ABC):

    def __init__(self):
        self.__title: str
        self.__library_id: str


    @property
    def library_id(self):
        return self.__library_id

    @library_id.setter
    def library_id(self, value):
        self.__library_id = value

    @property
    def title(self):
        return self.__title

    @title.setter
    def title(self, value):
        self.__title = value


