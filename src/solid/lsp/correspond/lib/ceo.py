from src.solid.lsp.correspond.lib.interface_manager import IManager
from src.solid.lsp.correspond.lib.base_employee import BaseEmployee


class CEO(BaseEmployee, IManager):

    def __init__(self):
        BaseEmployee.__init__(self)

    def calculate_per_hour_rate(self, rank):
        base_amount = 150
        self.salary = base_amount * rank

    def generate_performance_review(self):
        print("I'm reviewing a direct report's performance.")

    def fire_someone(self):
        print("You're Fired!")
