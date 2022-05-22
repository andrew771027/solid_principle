class Person:

    __firstname = None
    __lastname = None
    __phone_number = None
    __email_address = None

    def __init__(self, firstname, lastname, phone_number, email_address):
        self.firstname = firstname
        self.lastname = lastname
        self.phone_number = phone_number
        self.email_address = email_address

    @property
    def firstname(self):
        return self.__firstname

    @firstname.setter
    def firstname(self, value):
        self.__firstname = value

    @property
    def lastname(self):
        return self.__lastname

    @lastname.setter
    def lastname(self, value):
        self.__lastname = value

    @property
    def phone_number(self):
        return self.__phone_number

    @phone_number.setter
    def phone_number(self, value):
        self.__phone_number = value

    @property
    def email_address(self):
        return self.__email_address

    @email_address.setter
    def email_address(self, value):
        self.__email_address = value
