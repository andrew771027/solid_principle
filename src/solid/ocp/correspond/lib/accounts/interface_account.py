import abc
from src.solid.ocp.correspond.lib.employee_model import EmployeeModel


class IAccounts(abc.ABC):

    def create(self, person) -> EmployeeModel:
        raise NotImplementedError
