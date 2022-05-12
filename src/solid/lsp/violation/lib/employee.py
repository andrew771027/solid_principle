from decimal import *


class Employee:

    def __init__(self):
        self.__firstname: str = None
        self.__lastname: str = None
        self.__manager = None
        self.__salary: Decimal = None

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

    @property
    def manager(self):
        return self.__manager

    @manager.setter
    def manager(self, value):
        self.__manager = value

    @property
    def salary(self):
        return self.__salary

    @salary.setter
    def salary(self, value):
        self.__salary = value

    def assign_manager(self, manager):
        self.manager = manager

    def calculate_per_hour_rate(self, rank):
        base_amount = 12.50
        self.salary = base_amount + (rank * 2)
