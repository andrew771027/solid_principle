import abc
from src.solid.dip.correspond.lib.iperson import IPerson


class IMessageSender(abc.ABC):

    def send_message(self, person: IPerson, message: str):
        raise NotImplementedError
