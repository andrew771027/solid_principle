
from src.solid.ocp.correspond.lib.applicants.interface_applicant_model import IApplicantModel
from src.solid.ocp.correspond.lib.accounts.interface_account import IAccounts
from src.solid.ocp.correspond.lib.accounts.person_accounts import PersonAccount


class PersonModel(IApplicantModel):

    account_processor: IAccounts = PersonAccount()

    def __init__(self, firstname, lastname):
        super().__init__(firstname, lastname)
