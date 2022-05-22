from src.solid.dip.violation.lib.person import Person


class Emailer:

    def send_message(self, person: Person, message: str):

        print(f"Simulating sending an email to {person.email_address}")
