from src.solid.ocp.correspond.lib.employee_model import EmployeeModel
from src.solid.ocp.correspond.lib.accounts.interface_account import IAccounts


class PersonAccount(IAccounts):

    def create(self, person) -> EmployeeModel:

        output: EmployeeModel = EmployeeModel()
        output.firstname = person.firstname
        output.lastname = person.lastname
        output.email_address = f'{person.firstname[0]}{person.lastname}@test.com'

        return output
