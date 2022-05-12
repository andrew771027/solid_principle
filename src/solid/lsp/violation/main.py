from src.solid.lsp.violation.lib.employee import Employee
from src.solid.lsp.violation.lib.manager import Manager
from src.solid.lsp.violation.lib.ceo import CEO


def main():

    accountingVP: Manager = Manager()
    accountingVP.firstname = "Emma"
    accountingVP.lastname = "Stone"
    accountingVP.calculate_per_hour_rate(4)

    emp: Employee = Employee()
    emp.firstname = "Tim"
    emp.lastname = "Wang"
    emp.assign_manager(accountingVP)
    emp.calculate_per_hour_rate(2)

    print(f"{emp.firstname}'s salary is {emp.salary}/hour.")
