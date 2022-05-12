class Person:
    first_name = None
    last_name = None


def main():
    # Standard Messages
    print("Welcome to my application", end="\n")

    # Person Data
    user = Person()

    # Capture
    user.first_name = input("What is your first name: ")
    user.last_name = input("What is your last name: ")

    # Personal Data Validation
    if user.first_name is None:
        print("You did not give a valid first name.")
        # Standard Messages
        print("\n")
        return

    # Personal Data Validation
    if user.last_name is None:
        print("You did not give a valid last name.")
        # Standard Messages
        print("\n")
        return

    # Account Generator
    print(f"Your name is {user.first_name} {user.last_name}", end="")

    # Standard Messages
    print("\n")
