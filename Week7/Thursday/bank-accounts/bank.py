import csv
from account import Account
from owner import Owner


class Bank:
    
    def __init__(self):
        self.members = Owner.all_members()
        self.accounts = Account.all_accounts()
        self.member_account_relationsip()
        self.next_member_number = 1

        

    def create_member(self, first_name, last_name, street_address, city, state):
        self.members[self.next_member_number] = Owner(first_name, last_name,street_address, city, state, self.next_member_number)
        self.next_member_number += 1
        return self.members

    def create_account(self, member_id ,opening_balance, open_date):
        if not self.members[member_id]:
            print('no such memember')
            member_id = self.next_member_number
            self.create_member(**self.new_member_data())
        member = self.members[member_id]
        member.accounts[member.account_numbers] = (Account(member_id, opening_balance, open_date))
        member.account_numbers += 1

    def new_member_data(self):
        data = {}
        data['first_name'] = input("Enter member's first name:\n")
        data['last_name'] = input("Enter member's last name\n")
        data['street_address'] = input("Enter member's street address\n")
        data['city'] = input("Enter member's city\n")
        data['state'] = input("Enter member's state\n")
        return data

    
    def member_account_relationsip(self):
        with open('support/account_owners.csv') as csvfile:
            relations = csv.reader(csvfile)
            for r in relations:
                member_id = int(r[1])
                account_id = int(r[0])
                member = self.members[member_id]
                account = self.accounts[account_id]
                member.accounts[account_id] = account
    
