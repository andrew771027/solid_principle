from standard_messages import StandardMessages
from person_data import Person
from person_data_capture import PersonDataCapture
from person_data_validation import PersonDataValidator
from account_generator import AccountGenerator


def main():

    StandardMessages.WelcomeMessage()

    user: Person = PersonDataCapture.capture()

    isValid: bool = PersonDataValidator.validate(user)

    if isValid == False:
        StandardMessages.EndApplicationMessage()
        return

    AccountGenerator.create_account(user)

    StandardMessages.EndApplicationMessage()


if __name__ == '__main__':
    main()
