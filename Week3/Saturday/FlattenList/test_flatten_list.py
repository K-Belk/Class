import unittest
from flatten_list import flatten_list

class TestFlatten(unittest.TestCase):

    def test_flattend(self):
        self.assertEqual(flatten_list([1, 2, [3], [4,5]]), [1,2,3,4,5])

    def test_flattend_deep_nest(self):
        self.assertEqual(flatten_list([1, [2], [3, [4, 5, [6]]], 7]), [1, 2, 3, 4, 5, 6, 7])

    def test_is_a_list(self):
        self.assertEqual(flatten_list({2:4}), 'not a list')

    def test_string_list(self):
        self.assertEqual(flatten_list(['tacos','nachos', ['burrito', 'fajitas'], 'carnitas']), ['tacos','nachos', 'burrito', 'fajitas', 'carnitas'])

if __name__ == '__main__':
    unittest.main() 

# @classmethod
# seuUpClass(cls) # runs once at the beginning

# return super().setUpClass()

# seUp(self) runs before every test