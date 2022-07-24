from argparse import ArgumentError
from account import Account


class Savings(Account):

    def __init__(self, account_id, initial_balance, open_date):
        super().__init__(account_id, initial_balance, open_date)
        if initial_balance < 10:
            raise ArgumentError(None, 'No')

    def withdraw(self, amount):
        amount += 2
        if (self.balance - amount) < 10:
            print("Insufficient funds. ")
            return self.balance
        return super().withdraw(amount)

    def add_interest(self, rate=.25):
        self.balance = self.balance * rate/100
        return self.balance