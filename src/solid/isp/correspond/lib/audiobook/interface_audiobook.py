
from src.solid.isp.correspond.lib.general_interface.interface_library_item import LibraryItemInterface


class AudioBookInterface(LibraryItemInterface):
    def __init__(self):
        super().__init__()
        self.__run_time_in_minutes: int

    @property
    def run_time_in_minutes(self):
        return self.__run_time_in_minutes

    @run_time_in_minutes.setter
    def run_time_in_minutes(self, value):
        self.__run_time_in_minutes = value
