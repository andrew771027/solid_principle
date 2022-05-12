import abc
from datetime import datetime


class LibraryItemInterface(abc.ABC):

    def __init__(self):
        self.__author: str
        self.__borrow_date: datetime
        self.__borrower: str
        self.__checkout_duration_in_days: int
        self.__library_id: str
        self.__pages: int
        self.__title: str

    @property
    def author(self):
        return self.__author

    @author.setter
    def author(self, value):
        self.__author = value

    @property
    def borrow_date(self):
        return self.__borrow_date

    @borrow_date.setter
    def borrow_date(self, value):
        self.__borrow_date = value

    @property
    def borrower(self):
        return self.__borrower

    @borrower.setter
    def borrower(self, value):
        self.__borrower = value

    @property
    def checkout_duration_in_days(self):
        return self.__checkout_duration_in_days

    @checkout_duration_in_days.setter
    def checkout_duration_in_days(self, value):
        self.__checkout_duration_in_days = value

    @property
    def library_id(self):
        return self.__library_id

    @library_id.setter
    def library_id(self, value):
        self.__library_id = value

    @property
    def pages(self):
        return self.__pages

    @pages.setter
    def pages(self, value):
        self.__pages = value

    @property
    def title(self):
        return self.__title

    @title.setter
    def title(self, value):
        self.__title = value

    @abc.abstractmethod
    def check_in(self):
        raise NotImplementedError

    @abc.abstractmethod
    def check_out(self, borrower: str):
        raise NotImplementedError

    @abc.abstractmethod
    def get_due_date(self):
        raise NotImplementedError
