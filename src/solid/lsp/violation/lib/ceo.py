from src.solid.lsp.violation.lib.employee import Employee


class CEO(Employee):

    def __init__(self):
        super().__init__()

    def calculate_per_hour_rate(self, rank):
        base_amount = 150
        self.salary = base_amount * rank

    def assign_manager(self, manager):
        raise ValueError("The CEO has no manager.")

    def generate_performance_review(self):
        print("I'm reviewing a direct report's performance.")

    def fire_someone(self):
        print("You're Fired!")
