from src.solid.ocp.correspond.lib.applicants.interface_applicant_model import IApplicantModel
from src.solid.ocp.correspond.lib.accounts.interface_account import IAccounts
from src.solid.ocp.correspond.lib.accounts.manager_accounts import ManagerAccount


class ManagerModel(IApplicantModel):

    account_processor: IAccounts = ManagerAccount()

    def __init__(self, firstname, lastname):
        super().__init__(firstname, lastname)

    @property
    def is_manager(self):
        return self.__is_manager

    @is_manager.setter
    def is_manager(self, value: bool):
        self.__is_manager = value
