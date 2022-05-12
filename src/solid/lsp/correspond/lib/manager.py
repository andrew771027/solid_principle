from src.solid.lsp.correspond.lib.base_employee import BaseEmployee
from src.solid.lsp.correspond.lib.interface_manager import IManager
from src.solid.lsp.correspond.lib.interface_managed import IManaged


class Manager(BaseEmployee, IManager, IManaged):

    def __init__(self):
        self.__manager = None
        BaseEmployee.__init__(self)

    def calculate_per_hour_rate(self, rank):
        base_amount = 19.75
        self.salary = base_amount + (rank * 4)

    def generate_performance_review(self):
        print("I'm reviewing a direct report's performance.")
