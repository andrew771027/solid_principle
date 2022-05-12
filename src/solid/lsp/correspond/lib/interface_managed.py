import abc
from src.solid.lsp.correspond.lib.interface_employee import IEmployee


class IManaged:

    @property
    def manager(self):
        return self.__manager

    @manager.setter
    def manager(self, value):
        self.__manager = value

    def assign_manager(self, manager):
        self.manager = manager
