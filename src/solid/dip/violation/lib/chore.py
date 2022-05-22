from src.solid.dip.violation.lib.person import Person
from src.solid.dip.violation.lib.emailer import Emailer
from src.solid.dip.violation.lib.logger import Logger


class Chore:

    __chore_name = None
    __owner: Person = None
    __hours_worked = None
    __is_complete = None

    def __init__(self, chore_name, owner: Person):
        self.chore_name = chore_name
        self.owner = owner

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
    def owner(self, value: Person):
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
        log = Logger()
        log.Log(f"Performed work on {self.chore_name}")

    def complete_chore(self):
        self.is_complete = True

        log = Logger()
        log.Log(f"Completed {self.chore_name}")

        emailer = Emailer()
        emailer.send_message(
            self.owner, f"The chore {self.chore_name} is complete")
