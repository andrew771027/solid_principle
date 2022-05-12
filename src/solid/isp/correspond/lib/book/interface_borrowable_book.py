from src.solid.isp.correspond.lib.general_interface.interface_borrowable import BorrowableInterface
from src.solid.isp.correspond.lib.book.interface_book import BookInterface


class BorrowableBookInterface(BorrowableInterface, BookInterface):

    def __init__(self):
        BorrowableInterface.__init__()
        BookInterface.__init__()
