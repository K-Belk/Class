import unittest

from balanced_parentheses import Balance

class BalancedParentheseTest(unittest.TestCase):

    def test_one(self):
        one = Balance("()")
        self.assertEqual(one.string, "()")
    def test_two(self):
        two = Balance("a(b)c)")
        self.assertEqual(two.string, "a(b)c")
    def test_three(self):
        three = Balance("(a)(bdd)c)")
        self.assertEqual(three.string, "(a)(bdd)c")
    def test_four(self):
        four = Balance("a(dbvb)c)")
        self.assertEqual(four.string, "a(dbvb)c")
    def test_five(self):
        five = Balance("a(b)(c)())")
        self.assertEqual(five.string, "a(b)(c)()")
    def test_six(self):
        six = Balance(")(")
        self.assertEqual(six.string, "")
    def test_seven(self):
        seven = Balance("(((((")
        self.assertEqual(seven.string, '')
    def test_eight(self):
        eight = Balance(")(())(")
        self.assertEqual(eight.string, "(())")
    def test_nine(self):
        nine = Balance("(()()(")
        self.assertEqual(nine.string, "()()")
    def test_ten(self):
        ten = Balance("(()()(")
        self.assertEqual(ten.string, "()()")

if __name__ == '__main__':
    unittest.main()
