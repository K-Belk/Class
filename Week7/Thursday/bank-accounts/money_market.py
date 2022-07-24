from argparse import ArgumentError
from account import Account

class MoneyMarket(Account):

    def __init__(self, account_id, initial_balance, open_date):
        super().__init__(account_id, initial_balance, open_date)
        self.transactions = 0
        self.hold = False
        if initial_balance < 10000:
            raise ArgumentError(None, "Insufficient funds to open account")

    def withdraw(self, amount):
        if self.hold == False and self.transactions < 6:
            self.balance -= amount
            self.transactions += 1
            if self.balance < 10000:
                self.balance -= 100
                self.hold = True
            return self.balance
        
    def deposit(self, amount):
        if self.transactions < 6:
            if self.hold == True and (amount + self.balance) >= 10000:
                self.hold = False
                return super().deposit(amount)
            self.transactions += 1
            return super().deposit(amount)

    def reset_transactions(self):
        self.transactions = 0
        return self.transactions
