from account import Account

class Checking(Account):

    def __init__(self, account_id, initial_balance, open_date):
        super().__init__(account_id, initial_balance, open_date)
        self.free_checks = 0

    def withdraw(self, amount):
        amount += 1
        if (self.balance - amount)< 0:
            print("Insufficient funds.")
            return self.balance
        return super().withdraw(amount)

    def withdraw_using_check(self, amount):
        self.free_checks += 1
        if self.free_checks > 3:
            amount += 2
        if (self.balance - amount) < -10:
            return self.balance
        else:
            self.balance -= amount
            return self.balance

    def reset_checks(self):
        self.free_checks = 0
        return self.free_checks