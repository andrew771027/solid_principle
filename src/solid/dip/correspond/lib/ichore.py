import abc
from src.solid.dip.correspond.lib.iperson import IPerson


class IChore(abc.ABC):

    __chore_name = None
    __owner: IPerson = None
    __hours_worked = None
    __is_complete = None

    @property
    @abc.abstractproperty
    def chore_name(self):
        raise NotImplementedError

    @chore_name.setter
    @abc.abstractmethod
    def chore_name(self, value):
        raise NotImplementedError

    @property
    @abc.abstractproperty
    def owner(self):
        raise NotImplementedError

    @owner.setter
    @abc.abstractmethod
    def owner(self, value: IPerson):
        raise NotImplementedError

    @property
    @abc.abstractproperty
    def hours_worked(self):
        raise NotImplementedError

    @owner.setter
    @abc.abstractmethod
    def hours_worked(self, value):
        raise NotImplementedError

    @property
    @abc.abstractproperty
    def is_complete(self):
        raise NotImplementedError

    @is_complete.setter
    @abc.abstractmethod
    def is_complete(self, value):
        raise NotImplementedError

    @abc.abstractmethod
    def performed_work(self, hours):
        raise NotImplementedError

    @abc.abstractmethod
    def complete_chore(self):
        raise NotImplementedError
