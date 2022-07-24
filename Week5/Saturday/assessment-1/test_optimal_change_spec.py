import unittest
from optimal_change import optimal_change



class TestStringMethods(unittest.TestCase):

    def test_is_string(self):
        self.assertEqual(type(optimal_change(.99, 1)), str)

    def test_one_penny(self):
        self.assertEqual(optimal_change(.99, 1), 'The optimal change for an item that costs $0.99 with an amount paid of $1 is 1 penny.')

    def test_38_dollars_and_eighty_seven_cents(self):
        self.assertEqual(optimal_change(62.13, 100), "The optimal change for an item that costs $62.13 with an amount paid of $100 is 1 $20 bill, 1 $10 bill, 1 $5 bill, 2 $1 bills, 3 quarters, 1 dime, and 2 pennies.")

    def test_eighteen_dollars_and_fourtie_nine_cents(self):
        self.assertEqual(optimal_change(31.51, 50), "The optimal change for an item that costs $31.51 with an amount paid of $50 is 1 $10 bill, 1 $5 bill, 3 $1 bills, 1 quarter, 2 dimes, and 4 pennies.")

    def test_five_hundred_nine_dollars_seventy_one_cents(self):
        self.assertEqual(optimal_change(51.69, 561.40), "The optimal change for an item that costs $51.69 with an amount paid of $561.4 is 5 $100 bills, 1 $5 bill, 4 $1 bills, 2 quarters, 2 dimes, and 1 penny.")
    
    def test_no_change(self):
        self.assertEqual(optimal_change(51, 51), "There is no change for an item that costs $51 with an amount paid of $51.")

    def test_string_input(self):
        self.assertEqual(type(optimal_change(".99", "1")), str)

if __name__ == '__main__':
    unittest.main()
