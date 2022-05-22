import abc


class IPerson(abc.ABC):

    __firstname = None
    __lastname = None
    __phone_number = None
    __email_address = None

    @property
    @abc.abstractproperty
    def firstname(self):
        raise NotImplementedError

    @firstname.setter
    @abc.abstractmethod
    def firstname(self, value):
        raise NotImplementedError

    @property
    @abc.abstractproperty
    def lastname(self):
        raise NotImplementedError

    @lastname.setter
    @abc.abstractmethod
    def lastname(self, value):
        raise NotImplementedError

    @property
    @abc.abstractproperty
    def phone_number(self):
        raise NotImplementedError

    @phone_number.setter
    @abc.abstractmethod
    def phone_number(self, value):
        raise NotImplementedError

    @property
    @abc.abstractproperty
    def email_address(self):
        raise NotImplementedError

    @email_address.setter
    @abc.abstractmethod
    def email_address(self, value):
        raise NotImplementedError
