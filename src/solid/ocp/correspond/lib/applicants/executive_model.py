from src.solid.ocp.correspond.lib.applicants.interface_applicant_model import IApplicantModel
from src.solid.ocp.correspond.lib.accounts.interface_account import IAccounts
from src.solid.ocp.correspond.lib.accounts.executive_accounts import ExecutiveAccount


class ExecutiveModel(IApplicantModel):

    account_processor: IAccounts = ExecutiveAccount()

    def __init__(self, firstname, lastname):
        super().__init__(firstname, lastname)

    @property
    def is_manager(self):
        return self.__is_manager

    @is_manager.setter
    def is_manager(self, value: bool):
        self.__is_manager = value

    @property
    def is_executive(self):
        return self.__is_executive

    @is_executive.setter
    def is_executive(self, value: bool):
        self.__is_executive = value
