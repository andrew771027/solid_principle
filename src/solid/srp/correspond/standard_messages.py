class StandardMessages:

    @staticmethod
    def WelcomeMessage():
        print("Welcome to my application", end="\n")

    @staticmethod
    def EndApplicationMessage():
        print("Application End...")

    @staticmethod
    def ValidationErrorMessage(field_name: str):
        print(f"You did not give a valid {field_name}.")
