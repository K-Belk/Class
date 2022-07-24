import unittest
from char_count import char_count

class TestCharCount(unittest.TestCase):


    def test_one(self):
        self.assertEqual(char_count("aaabbc"), {
            "a": 3,
            "b": 2,
            "c": 1
            })

    def test_two(self):
        self.assertEqual(char_count("an apple a day will keep the doctor away"), {
            "a":6,
            "e":4,
            "l":3,
            "p":3,
            "w":2,
            "d":2,
            "o":2,
            "t":2,
            "y":2,
            "k":1,
            "h":1,
            "i":1,
            "c":1,
            "n":1,
            "r":1
            })

if __name__ == '__main__':
    unittest.main()