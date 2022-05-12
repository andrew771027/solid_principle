import abc
from typing import List
from src.solid.isp.correspond.lib.general_interface.interface_library_item import LibraryItemInterface


class DVDInterface(LibraryItemInterface):

    def __init__(self):
        self.__actors: List[str]
        self.__run_time_in_minutes: int

    @property
    def actors(self):
        return self.__actors

    @actors.setter
    def actors(self, value):
        self.__actors = value

    @property
    def run_time_in_minutes(self):
        return self.__run_time_in_minutes

    @run_time_in_minutes.setter
    def run_time_in_minutes(self, value):
        self.__run_time_in_minutes = value
