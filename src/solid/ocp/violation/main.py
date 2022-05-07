from typing import List
from src.solid.ocp.violation.lib.person_model import PersonModel
from src.solid.ocp.violation.lib.employee_model import EmployeeModel
from src.solid.ocp.violation.lib.accounts import Account
from src.solid.ocp.violation.lib.employee_types import EmployeeType
'''
1. Add a new type of employee Manager
2. Add a new type of employee Executive
'''


def main():

    applicants: List[PersonModel] = []
    applicants.append(PersonModel(**{'firstname': 'Tim', 'lastname': 'Zhang'}))
    applicants.append(PersonModel(
        **{'firstname': 'Andrew', 'lastname': 'Wang', 'type_of_employee': EmployeeType.MANAGER}))
    applicants.append(PersonModel(
        **{'firstname': "Nancy", 'lastname': "Lee", 'type_of_employee': EmployeeType.EXECUTIVE}))

    employees: List[EmployeeModel] = []
    account_processor = Account()

    for person in applicants:
        employees.append(account_processor.create(person))

    for emp in employees:
        print(
            f"{emp.firstname} {emp.lastname}: {emp.email_address} Is Manager: {emp.is_manager} Is Executive: {emp.is_executive}")
