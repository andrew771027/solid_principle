from src.solid.dip.correspond.lib.iperson import IPerson
from src.solid.dip.correspond.lib.person import Person
from src.solid.dip.correspond.lib.ichore import IChore
from src.solid.dip.correspond.lib.chore import Chore
from src.solid.dip.correspond.lib.imessage_sender import IMessageSender
from src.solid.dip.correspond.lib.emailer import Emailer
from src.solid.dip.correspond.lib.ilogger import ILogger
from src.solid.dip.correspond.lib.logger import Logger
from src.solid.dip.correspond.lib.texter import Texter


class Factory:

    @staticmethod
    def CreatePerson() -> IPerson:
        return Person()

    @staticmethod
    def CreateChore(cls) -> IChore:
        return Chore(cls.CreateLogger(), cls.CreateMessageSender())

    @staticmethod
    def CreateEmailer() -> IMessageSender:
        return Emailer()

    @staticmethod
    def CreateLogger() -> ILogger:
        return Logger()

    @staticmethod
    def CreateMessageSender() -> IMessageSender:
        return Texter()
