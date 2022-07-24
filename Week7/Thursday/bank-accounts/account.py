import csv
from datetime import datetime


class Account:

    def __init__(self, account_id, initial_balance, open_date):
        if initial_balance < 0:
            raise Exception('Cannot open an account with a negative balance')
        self.account_id = account_id
        self.balance = initial_balance
        self.open_date = open_date

    def withdraw(self, amount):
        if amount > self.balance:
            return f"Insufficient funds. Current balance is {self.balance}"
        else:
            self.balance -= amount
            return self.balance

    def deposit(self, amount):
        self.balance += amount
        return self.balance


    @classmethod
    def all_accounts(cls):
        acc = {}
        with open('support/accounts.csv') as csvfile:
            accounts = csv.reader(csvfile)
            for a in accounts:
                hold = {}
                hold['account_id'] = int(a[0])
                hold['initial_balance'] = int(a[1])
                hold['open_date'] = a[2]
                acc[int(a[0])] = Account(**hold)
        return acc

    @classmethod
    def find(self, account_id):
        with open('support/accounts.csv') as csvfile:
            accounts = csv.reader(csvfile)
            for id in accounts:
                if id[0] == str(account_id):
                    found = {}
                    found['account_id'] = int(id[0])
                    found['initial_balance'] = int(id[1])
                    found['open_date'] = id[2]
                    return found
            return "No account found"