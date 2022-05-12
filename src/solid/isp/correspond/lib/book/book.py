from datetime import datetime
from src.solid.isp.correspond.lib.book.interface_borrowable_book import BorrowableBookInterface


class Book(BorrowableBookInterface):

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