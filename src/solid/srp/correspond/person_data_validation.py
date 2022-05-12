from attr import fields_dict
from src.solid.srp.correspond.person_data import Person
from src.solid.srp.correspond.standard_messages import StandardMessages


class PersonDataValidator:

    @staticmethod
    def validate(user: Person):

        if user.first_name is None or user.first_name == "":
            # Standard Message
            StandardMessages.ValidationErrorMessage(field_name="first name")
            StandardMessages.EndApplicationMessage()
            return False

        if user.last_name is None or user.last_name == "":
            # Standard Mesage
            StandardMessages.ValidationErrorMessage(field_name="last name")
            StandardMessages.EndApplicationMessage()
            return False

        return True
