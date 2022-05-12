from datetime import datetime
from src.solid.isp.violation.lib.interface_library_item import LibraryItemInterface


class AudioBook(LibraryItemInterface):

    def __init__(self):
        super().__init__()
        self.__run_time_in_minutes: int

    @property
    def checkout_duration_in_days(self):
        return super().checkout_duration_in_days

    @checkout_duration_in_days.setter
    def checkout_duration_in_days(self, value=14):
        return super().checkout_duration_in_days(value)

    @property
    def pages(self):
        return super().pages

    @pages.setter
    def pages(self, value=-1):
        return super().pages(value)

    @property
    def run_time_in_minutes(self):
        return self.__run_time_in_minutes

    @run_time_in_minutes.setter
    def run_time_in_minutes(self, value):
        self.__run_time_in_minutes = value

    def check_out(self, borrower: str):
        self.borrower = borrower
        self.borrow_date = datetime.now()

    def check_in(self):
        self.borrower = ""

    def get_due_date(self):
        from datetime import timedelta
        return self.borrow_date + timedelta(days=self.checkout_duration_in_days)
