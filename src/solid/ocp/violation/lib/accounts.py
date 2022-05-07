from src.solid.ocp.violation.lib.person_model import PersonModel
from src.solid.ocp.violation.lib.employee_model import EmployeeModel
from src.solid.ocp.violation.lib.employee_types import EmployeeType


class Account:

    def create(self, person: PersonModel) -> EmployeeModel:

        output: EmployeeModel = EmployeeModel(**{
            'firstname': person.firstname,
            'lastname': person.lastname,
            'email_address': f'{person.firstname[0]}{person.lastname}@test.com',
            'is_manager': self.__is_manager(person.type_of_employee),
            'is_executive': self.__is_executive(person.type_of_employee)
        })
        return output

    def __is_manager(self, type_of_employee):

        if type_of_employee == EmployeeType.MANAGER:
            return True
        elif type_of_employee == EmployeeType.EXECUTIVE:
            return True
        return False

    def __is_executive(self, type_of_employee):
        if type_of_employee == EmployeeType.MANAGER:
            return False
        elif type_of_employee == EmployeeType.EXECUTIVE:
            return True
        return False
