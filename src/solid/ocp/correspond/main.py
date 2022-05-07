from typing import List
from src.solid.ocp.correspond.lib.applicants.person_model import PersonModel
from src.solid.ocp.correspond.lib.applicants.manager_model import ManagerModel
from src.solid.ocp.correspond.lib.applicants.executive_model import ExecutiveModel
from src.solid.ocp.correspond.lib.employee_model import EmployeeModel
from src.solid.ocp.correspond.lib.applicants.interface_applicant_model import IApplicantModel

'''
1. Add a new type of employee Manager
2. Add a new type of employee Executive
'''


def main():

    applicants: List[IApplicantModel] = []
    applicants.append(PersonModel(firstname='Tim', lastname='Zhang'))
    applicants.append(ManagerModel(firstname='Andrew', lastname='Wang'))
    applicants.append(ExecutiveModel(firstname="Nancy", lastname="Lee"))

    employees: List[EmployeeModel] = []

    for person in applicants:
        employees.append(person.account_processor.create(person))

    for emp in employees:
        print(
            f"{emp.firstname} {emp.lastname}: {emp.email_address} Is Manager: {emp.is_manager} Is Executive: {emp.is_executive}")
