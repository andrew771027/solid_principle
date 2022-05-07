class EmployeeModel:

    def __init__(self):
        self.__firstname: str = None
        self.__lastname: str = None
        self.__email_address: str = None
        self.__is_manager: bool = False
        self.__is_executive: bool = False

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
    def email_address(self):
        return self.__email_address

    @email_address.setter
    def email_address(self, value):
        self.__email_address = value

    @property
    def is_manager(self):
        return self.__is_manager

    @is_manager.setter
    def is_manager(self, value: bool):
        self.__is_manager = value

    @property
    def is_executive(self):
        return self.__is_executive

    @is_executive.setter
    def is_executive(self, value: bool):
        self.__is_executive = value
