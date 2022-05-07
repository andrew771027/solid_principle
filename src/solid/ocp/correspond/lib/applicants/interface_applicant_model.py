import abc
from src.solid.ocp.correspond.lib.accounts.interface_account import IAccounts


class IApplicantModel(abc.ABC):

    account_processor: IAccounts = None

    def __init__(self, firstname, lastname):
        self.__firstname: str = firstname
        self.__lastname: str = lastname

    @property
    def firstname(self):
        return self.__firstname

    @firstname.setter
    def firstname(self, value):
        self.__firstname = value

    @property
    def lastname(self):
        return self.__lastname

    @lastname.setter
    def lastname(self, value):
        self.__lastname = value
