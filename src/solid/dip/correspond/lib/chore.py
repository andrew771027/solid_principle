from telnetlib import IP
from src.solid.dip.correspond.lib.ichore import IChore
from src.solid.dip.correspond.lib.iperson import IPerson
from src.solid.dip.correspond.lib.ilogger import ILogger
from src.solid.dip.correspond.lib.imessage_sender import IEmailer


class Chore(IChore):

    __logger: ILogger = None
    __message_sender: IEmailer = None

    def __init__(self, logger: ILogger, message_sender: IEmailer):
        super().__init__()
        self.__logger = logger
        self.__message_sender = message_sender

    @property
    def chore_name(self):
        return self.__chore_name

    @chore_name.setter
    def chore_name(self, value):
        self.__chore_name = value

    @property
    def owner(self):
        return self.__owner

    @owner.setter
    def owner(self, value: IPerson):
        self.__owner = value

    @property
    def hours_worked(self):
        return self.__hours_worked

    @owner.setter
    def hours_worked(self, value):
        self.__hours_worked = value

    @property
    def is_complete(self):
        return self.__is_complete

    @is_complete.setter
    def is_complete(self, value):
        self.__is_complete = value

    def performed_work(self, hours):
        self.hours_worked += hours
        self.__logger.Log(f"Performed work on {self.chore_name}")

    def complete_chore(self):
        self.is_complete = True
        self.__logger.Log(f"Completed {self.chore_name}")
        self.__message_sender.send_message(
            self.owner, f"The chore {self.chore_name} is complete")
