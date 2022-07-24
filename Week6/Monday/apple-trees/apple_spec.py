import unittest
from apple import *

class ValidateAppleClass(unittest.TestCase):
    """Tests for `apple.py`."""

    def test_apple_diameter(self):
        """When you create an Apple, it will have a diameter greater than 0"""
        apple = Apple()
        self.assertGreater(apple.diameter, 0)

if __name__ == '__main__':
    unittest.main()
