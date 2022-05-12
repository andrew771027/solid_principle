import abc
from datetime import datetime


class BorrowableInterface(abc.ABC):

    def __init__(self):
        self.__borrow_date: datetime
        self.__borrower: str
        self.__checkout_duration_in_days: int
        

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



    @abc.abstractmethod
    def check_in(self):
        raise NotImplementedError

    @abc.abstractmethod
    def check_out(self, borrower: str):
        raise NotImplementedError

    @abc.abstractmethod
    def get_due_date(self):
        raise NotImplementedError

    @property
    def checkout_duration_in_days(self):
        return self.__checkout_duration_in_days

    @checkout_duration_in_days.setter
    def checkout_duration_in_days(self, value):
        self.__checkout_duration_in_days = value
