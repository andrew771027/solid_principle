import abc


class IEmployee(abc.ABC):

    def __init__(self):
        self.__firstname = None
        self.__lastname = None
        self.__salary = None

    @property
    @abc.abstractmethod
    def firstname(self):
        raise NotImplementedError

    @firstname.setter
    @abc.abstractmethod
    def firstname(self, value):
        raise NotImplementedError

    @property
    @abc.abstractmethod
    def lastname(self):
        raise NotImplementedError

    @lastname.setter
    @abc.abstractmethod
    def lastname(self, value):
        raise NotImplementedError

    @property
    @abc.abstractmethod
    def salary(self):
        raise NotImplementedError

    @salary.setter
    @abc.abstractmethod
    def salary(self, value):
        raise NotImplementedError

    @abc.abstractmethod
    def calculate_per_hour_rate(self, rank):
        raise NotImplementedError
