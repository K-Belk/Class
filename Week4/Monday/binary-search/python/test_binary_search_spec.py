from binary_search import binary_search
import unittest 

class TestBinarySearch(unittest.TestCase):

    def setUp(self):
        self.test_array = [1,2,3,4,5]
        self.super_big_array = [1,5,7,2,3,8,4,9]
        self.super_big_array.sort()

    def test_one_in_index_zero(self):
        self.assertEqual(binary_search(1, self.test_array), 0)

    def test_two_in_index_one(self):
        self.assertEqual(binary_search(2, self.test_array), 1)

    def test_three_in_index_two(self):
        self.assertEqual(binary_search(3, self.test_array), 2)

    def test_four_in_index_three(self):
        self.assertEqual(binary_search(4, self.test_array), 3)

    def test_five_in_index_four(self):
        self.assertEqual(binary_search(5, self.test_array), 4)

    def test_seven_in_big_index_five(self):
        self.assertEqual(binary_search(7, self.super_big_array), 5)

    def test_six_not_in_big(self):
        self.assertEqual(binary_search(6, self.super_big_array), -1)


if __name__ == '__main__':
    unittest.main() 