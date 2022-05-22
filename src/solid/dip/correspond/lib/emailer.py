from src.solid.dip.correspond.lib.imessage_sender import IMessageSender
from src.solid.dip.correspond.lib.iperson import IPerson


class Emailer(IMessageSender):

    def send_message(self, person: IPerson, message: str):

        print(f"Simulating sending an email to {person.email_address}")
