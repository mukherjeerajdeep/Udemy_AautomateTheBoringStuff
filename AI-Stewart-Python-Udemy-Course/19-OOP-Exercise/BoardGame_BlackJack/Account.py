class Account:

    def __init__(self, name):
        self.name = name
        self.balance = 2000

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            print(f'{amount} is deposited, current balance is {self.balance}')

    def withdraw(self, amount):
        if not (self.balance > 0) and ((self.balance - amount) > 0):
            print(f"You don't have enough cash to withdraw you have {self.balance}, "
                  f"you wanted to withdraw {amount}")
            return False

        self.balance -= amount
        print(f"You withdrawn {amount} remaining cash {self.balance}")
        return True

    def __str__(self):
        return f'{self.name} currently has ${self.balance} in his account'


# account_test = Account("Tommy")
# print(f'deposited money {account_test.deposit(200)}')
#
# print(f'withdrawn money {account_test.withdraw(3200)}')
# print(f'withdrawn money {account_test.withdraw(1200)}')
#
# print(account_test)

# items = [1, 2, 3]
# print(*items, sep='\n')