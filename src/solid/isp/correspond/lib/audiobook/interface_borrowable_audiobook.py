from src.solid.isp.correspond.lib.audiobook.interface_audiobook import AudioBookInterface
from src.solid.isp.correspond.lib.general_interface.interface_borrowable import BorrowableInterface


class BorrowableAudioBookInterface(AudioBookInterface, BorrowableInterface):

    def __init__(self):
        AudioBookInterface.__init__()
        BorrowableInterface.__init__()
