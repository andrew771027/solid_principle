from src.solid.lsp.violation.lib.employee import Employee


class Manager(Employee):

    def __init__(self):
        super().__init__()

    def calculate_per_hour_rate(self, rank):
        base_amount = 19.75
        self.salary = base_amount + (rank * 4)

    def generate_performance_review(self):
        print("I'm reviewing a direct report's performance.")
