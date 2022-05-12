from src.solid.srp.correspond.standard_messages import StandardMessages
from src.solid.srp.correspond.person_data import Person
from src.solid.srp.correspond.person_data_capture import PersonDataCapture
from src.solid.srp.correspond.person_data_validation import PersonDataValidator
from src.solid.srp.correspond.account_generator import AccountGenerator


def main():

    StandardMessages.WelcomeMessage()

    user: Person = PersonDataCapture.capture()

    isValid: bool = PersonDataValidator.validate(user)

    if isValid == False:
        StandardMessages.EndApplicationMessage()
        return

    AccountGenerator.create_account(user)

    StandardMessages.EndApplicationMessage()

