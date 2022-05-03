from person_data import Person


class PersonDataCapture:

    @staticmethod
    def capture():
        user = Person()
        user.first_name = input("What is your first name: ")
        user.last_name = input("What is your last name: ")
        return user
