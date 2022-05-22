from src.solid.dip.violation.lib.person import Person
from src.solid.dip.violation.lib.chore import Chore


def main():

    owner: Person = Person(firstname='Andrew',
                           lastname="Wang",
                           email_address="hh@yopmail.com",
                           phone_number="0912345678")

    chore = Chore(chore_name="Take out the trash",
                  owner=owner)

    chore.performed_work(3)
    chore.performed_work(1.5)
    chore.complete_chore()
