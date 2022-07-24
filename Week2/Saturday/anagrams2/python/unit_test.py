import unittest
from anagram2 import anagrams_for


list_of_words = ["threads", "trashed", "hardest", "hatreds", "hounds"]

class TestStringMethods(unittest.TestCase):

    def test_one(self):
        self.assertEqual(anagrams_for("threads", list_of_words), ["threads", "trashed", "hardest", "hatreds"])

    def test_length(self):
        self.assertTrue(len(anagrams_for("threads", list_of_words)) == 4)
        

    def test_two(self):
        self.assertEqual(anagrams_for("apple", list_of_words), [])

if __name__ == '__main__':
    unittest.main()