from src.solid.dip.correspond.lib.imessage_sender import IMessageSender
from src.solid.dip.correspond.lib.iperson import IPerson


class Texter(IMessageSender):

    def send_message(self, person: IPerson, message: str):
        print(f"I'm texting {person.firstname} to say {message}")
