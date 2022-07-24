import unittest
from recursion_challenge import Recursive

class TestRecursion(unittest.TestCase):

    def setUp(self):
        self.recursion = Recursive()

    def test_factoral_4(self):
        self.assertEqual(self.recursion.factorial(4), 24)

    def test_factoral_8(self):
        self.assertEqual(self.recursion.factorial(8), 40320)

    def test_factoral_18(self):
        self.assertEqual(self.recursion.factorial(18), 6402373705728000)

    def test_factoral_45(self):
        self.assertEqual(self.recursion.factorial(45), 119622220865480194561963161495657715064383733760000000000)

    def test_palindrome_tacocat(self):
        self.assertEqual(self.recursion.palindrome('tacocat'), True)

    def test_palindrome_racecar(self):
        self.assertEqual(self.recursion.palindrome('racecar'), True)

    def test_palindrome_nice(self):
        self.assertEqual(self.recursion.palindrome('nice'), False)

    def test_palindrome_noon(self):
        self.assertEqual(self.recursion.palindrome('Nice'), False)

    def test_palindrome_sentence(self):
        self.assertEqual(self.recursion.palindrome('A man, a plan, a canal -- Panama'), True)

    def test_roman_3(self):
        self.assertEqual(self.recursion.roman_num(3), 'III')

    def test_roman_4(self):
        self.assertEqual(self.recursion.roman_num(4), 'IV')

    def test_roman_944(self):
        self.assertEqual(self.recursion.roman_num(944), 'CMXLIV')

    def test_roman_150(self):
        self.assertEqual(self.recursion.roman_num(150), 'CL')

    def test_roman_1(self):
        self.assertEqual(self.recursion.roman_num(1), 'I')

if __name__ == '__main__':
    unittest.main() 

