from src.solid.dip.correspond.lib.iperson import IPerson
from src.solid.dip.correspond.lib.ichore import IChore
from src.solid.dip.correspond.factory import Factory


def main():

    owner: IPerson = Factory.CreatePerson()

    owner.firstname = 'Andrew'
    owner.lastname = "Wang"
    owner.email_address = "hh@yopmail.com"
    owner.phone_number = "0912345678"

    chore: IChore = Factory.CreateChore()
    chore.chore_name = "Take out the trash"
    chore.owner = owner

    chore.performed_work(3)
    chore.performed_work(1.5)
    chore.complete_chore()
