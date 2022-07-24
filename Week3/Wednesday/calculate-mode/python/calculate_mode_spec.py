import unittest
from calculate_mode import calculate_mode

class TestCalculateMode(unittest.TestCase):

    def test_three_most(self):
        self.assertEqual(calculate_mode([1,2,3,3]), [3])

    def test_zero_most(self):
        self.assertEqual(calculate_mode([4.5, 0, 0]), [0])

    def test_one_point_five_most(self):
        self.assertEqual(calculate_mode([1.5, -1, 1, 1.5]), [1.5])

    def test_one_and_two_most(self):
        self.assertEqual(calculate_mode([1,1,2,2]), [1,2])

    def test_one_two_three_most(self):
        self.assertEqual(calculate_mode([1,2,3]), [1,2,3])

    def test_who_most(self):
        self.assertEqual(calculate_mode(["who", "what", "where", "who"]), ["who"])

if __name__ == '__main__':
    unittest.main()