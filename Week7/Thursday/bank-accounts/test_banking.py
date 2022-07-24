
from argparse import ArgumentError
import unittest
from unittest.mock import patch
from account import Account
from bank import Bank
from checking import Checking
from money_market import MoneyMarket
from owner import Owner
from savings_account import Savings

class TestStringMethods(unittest.TestCase):

    def test_account_open_negative(self):
        """Raises an error if account is created with a negative balance"""
        with self.assertRaises(Exception):
            Account(1, -500.00, '2022-01-01')

    def test_account_withdraw(self):
        """Withdrawing changes account balance"""
        ac = Account(1, 500.00, '2022-01-01')
        self.assertEqual(ac.withdraw(100), 400.00)

    def test_account_deposit(self):
        """Deposit adds value to account balance"""
        ac = Account(1, 500.00, '2022-01-01')
        self.assertEqual(ac.deposit(100), 600.00)

    def test_add_member(self):
        """Adds new member to members"""
        fake_data = {'first_name': 'Kevin', 'last_name': 'Belk', 'street_address': '123 Sesame ST', 'city': 'Springfield', 'state': 'gas'  }
        b = Bank()
        previous = len(b.members)
        b.create_member(**fake_data)
        self.assertEqual(len(b.members), previous + 1)

    def test_add_account_to_existing(self):
        """adds account to an existing member"""
        fake_data = {'first_name': 'Kevin', 'last_name': 'Belk', 'street_address': '123 Sesame ST', 'city': 'Springfield', 'state': 'gas'  }
        b = Bank()
        b.create_member(**fake_data)
        b.create_account(1,1000.00, '2022-01-01')
        self.assertEqual(len(b.members[1].accounts), 1)

    def test_read_all_accounts(self):
        """Reads all the accounts from the CSV file"""
        accounts = Account.all_accounts()
        self.assertEqual(len(accounts), 12)

    def test_find_account(self):
        """Finds a account in accounts CSV file"""
        find = Account.find(1212)
        self.assertEqual(find['initial_balance'], 1235667)

    def test_read_all_members(self):
        """Reads all members from CSV file"""
        members = Owner.all_members()
        self.assertEqual(len(members), 12)

    def test_find_members(self):
        """Finds a member in owners CSV file"""
        find = Owner.find(14)
        self.assertEqual(find['member_id'], 14)

    def test_member_account_relationship(self):
        """Adds account to owner """
        b = Bank()
        member_account = b.members[25].accounts[1212]
        self.assertEqual(member_account.account_id, 1212)

    def test_savings_opened_less_than_min(self):
        """If attempting to open a savings account with less than $10 raise an ArgumentError"""
        with self.assertRaises(ArgumentError):
            Savings(1,5,'2022-1-1')

    def test_savings_witdrawl_below_ten(self):
        """Will not let you withdrawl if it will leave your balance below $10"""
        s = Savings(1,15,'2002-2-2')
        s.withdraw(10)
        self.assertEqual(s.balance, 15)

    def test_two_dollar_withdrawal_penalty(self):
        """Withdrawal incurs a $2 fee"""
        s = Savings(1,25,'2002-2-2')
        s.withdraw(10)
        self.assertEqual(s.balance, 13)

    def test_checking_withdraw_all(self):
        """Witdrawl to 0 with $1 penalty"""
        c = Checking(1,10,'2022-2-2')
        c.withdraw(9)
        self.assertEqual(c.balance, 0)

    def test_checking_withdrawl_with_check_overdraft(self):
        """Witdraw up to with a check -$10"""
        c = Checking(1,20,'2222-2-2')
        c.withdraw_using_check(30)
        self.assertEqual(c.balance, -10)

    def test_money_market_open_less_than_min(self):
        """Will not let you create with a initial balance of less than $10,000"""
        with self.assertRaises(ArgumentError):
            MoneyMarket(1,5,'2022-1-1')

    def test_money_market_withdrawl(self):
        """withdraws from balance and increments transactions"""
        mm = MoneyMarket(1,100000, '2022-2-2')
        mm.withdraw(10000)
        self.assertEqual(mm.transactions, 1)
        self.assertEqual(mm.balance, 90000)

    def test_money_market_withdraw_to_less_than_min(self):
        """Withdraw to less than $10,000 incurs a $100 penalty """
        mm = MoneyMarket(1,100000, '2022-2-2')
        mm.withdraw(90500)
        self.assertEqual(mm.transactions, 1)
        self.assertEqual(mm.hold, True)
        self.assertEqual(mm.balance, 9400)

    def test_money_market_withdrawl_transation_limit(self):
        """Can not withdrawl with a 6 transactions in a month"""
        mm = MoneyMarket(1,100000, '2022-2-2')
        mm.transactions = 6
        mm.withdraw(5)
        self.assertEqual(mm.balance, 100000)

    def test_money_market_withdrawl_on_hold(self):
        """With hold True cannot withdrawl"""
        mm = MoneyMarket(1,10000, '2022-2-2')
        mm.withdraw(500)
        self.assertEqual(mm.hold, True)
        mm.withdraw(100)
        self.assertEqual(mm.balance, 9400)

    def test_money_market_deposit(self):
        """Deposits to balance and increments transactions"""
        mm = MoneyMarket(1,100000, '2022-2-2')
        mm.deposit(10000)
        self.assertEqual(mm.transactions, 1)
        self.assertEqual(mm.balance, 110000)

    def test_money_market_deposit_to_min(self):
        """Deposit with a balance less than $10,000 to get over min """
        mm = MoneyMarket(1,100000, '2022-2-2')
        mm.withdraw(90500)
        self.assertEqual(mm.transactions, 1)
        self.assertEqual(mm.hold, True)
        self.assertEqual(mm.balance, 9400)
        mm.deposit(600)
        self.assertEqual(mm.hold, False)
        self.assertEqual(mm.balance, 10000)

    def test_money_market_deposit_transation_limit(self):
        """Can not deposit with a 6 transactions in a month"""
        mm = MoneyMarket(1,100000, '2022-2-2')
        mm.transactions = 6
        mm.deposit(5)
        self.assertEqual(mm.balance, 100000)


if __name__ == '__main__':
    unittest.main()