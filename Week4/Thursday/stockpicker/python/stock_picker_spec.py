# Rewrite this in Unit Test
import unittest
from stock_picker import picker

class TestStockPicker(unittest.TestCase):

    def test_profit_12(self):
        self.assertEqual(picker([17,3,6,9,15,8,6,1,10]), [1,4])

    def test_profit_15(self):
        self.assertEqual(picker([3,17,6,9,18,15,6,1,10]), [0,4])

    def test_profit_18(self):
        self.assertEqual(picker([1,17,6,9,8,15,6,3,19]), [0,8])

    def test_profit_9(self):
        self.assertEqual(picker([19,17,6,9,8,15,6,3,1]), [2,5])


# print(picker([19,17,6,9,8,15,6,3,1]) == [2,5])

if __name__ == '__main__':
    unittest.main()
