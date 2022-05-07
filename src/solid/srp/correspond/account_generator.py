from src.solid.srp.correspond.person_data import Person


class AccountGenerator:

    @staticmethod
    def create_account(user: Person):
        print(f"Your name is {user.first_name} {user.last_name}")
