'''
Single Responsibility Principle(SRP)
'''


# class Account:

#     def __init__(self, account_no: str):
#         self.account_no = account_no

#     def get_account_number(self):
#         return self.account_no

#     def save(self):
#         pass

class AccountDB:

    def get_account_number(self, _id):
        pass

    def account_save(self, obj):
        pass


class Account:

    def __init__(self, account_no: str):
        self.account_no = account_no
        self._db = AccountDB()

    def get_account_number(self):
        return self.account_no

    def get(self, _id):
        return self._db.get_account_number(_id=_id)
    
    def save(self):
        self._db.account_save(obj=self)
