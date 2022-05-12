from src.solid.isp.correspond.lib.general_interface.interface_borrowable import BorrowableInterface
from src.solid.isp.correspond.lib.dvd.interface_dvd import DVDInterface


class BorrowableDVDInterface(BorrowableInterface, DVDInterface):

    def __init__(self):
        BorrowableInterface.__init__()
        DVDInterface.__init__()
