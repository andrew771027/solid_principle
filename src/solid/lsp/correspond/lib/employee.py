from decimal import *
from src.solid.lsp.correspond.lib.interface_employee import IEmployee
from src.solid.lsp.correspond.lib.base_employee import BaseEmployee
from src.solid.lsp.correspond.lib.interface_managed import IManaged


class Employee(BaseEmployee, IManaged):

    def __init__(self):
        self.__manager = None
        BaseEmployee.__init__(self)

    def assign_manager(self, manager):
        self.manager = manager

    def calculate_per_hour_rate(self, rank):
        base_amount = 12.50
        self.salary = base_amount + (rank * 2)
