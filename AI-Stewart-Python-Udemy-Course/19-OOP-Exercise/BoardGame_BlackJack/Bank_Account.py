import Account

class BankAccount(Account):

    def __init__(self, name, account_type):
        super().__init__(name)
        self.account_type = account_type
        # self.lenders = []
        # self.lenders.append(name)

    # def __str__(self):
    #     return self.lenders


bank_account = BankAccount("Tommy", 'savings')


print(bank_account.withdraw(200))


