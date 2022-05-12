from typing import List
from src.solid.isp.violation.lib.interface_library_item import LibraryItemInterface
from datetime import datetime


class DVD(LibraryItemInterface):

    def __init__(self):
        super().__init__()
        self.__actors: List[str]

    @property
    def actors(self):
        return self.__actors

    @actors.setter
    def actors(self, value):
        self.__actors = value

    @property
    def checkout_duration_in_days(self):
        return super().checkout_duration_in_days

    @checkout_duration_in_days.setter
    def checkout_duration_in_days(self, value=14):
        return super().checkout_duration_in_days(value)

    def check_out(self, borrower: str):
        self.borrower = borrower
        self.borrow_date = datetime.now()

    def check_in(self):
        self.borrower = ""

    def get_due_date(self):
        from datetime import timedelta
        return self.borrow_date + timedelta(days=self.checkout_duration_in_days)
