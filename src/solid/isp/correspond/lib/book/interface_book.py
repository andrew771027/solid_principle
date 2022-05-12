import abc
from src.solid.isp.correspond.lib.general_interface.interface_library_item import LibraryItemInterface


class BookInterface(LibraryItemInterface):

    def __init__(self):
        super().__init__()
        self.__author: str
        self.__pages: int

    @property
    def author(self):
        return self.__author

    @author.setter
    def author(self, value):
        self.__author = value

    @property
    def pages(self):
        return self.__pages

    @pages.setter
    def pages(self, value):
        self.__pages = value
