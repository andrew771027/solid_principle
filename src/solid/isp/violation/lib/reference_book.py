from src.solid.isp.violation.lib.interface_library_item import LibraryItemInterface


class ReferenceBook(LibraryItemInterface):

    def __init__(self):
        super().__init__()

    @property
    def checkout_duration_in_days(self):
        return super().checkout_duration_in_days

    @checkout_duration_in_days.setter
    def checkout_duration_in_days(self, value=0):
        return super().checkout_duration_in_days(value)

    def check_out(self, borrower: str):
        raise NotImplementedError

    def check_in(self):
        raise NotImplementedError

    def get_due_date(self):
        raise NotImplementedError
