import unittest, itertools
from apple_tree import *
from apple import *

class ValidateAppleTreeClass(unittest.TestCase):
    """Tests for `apple_tree.py`."""

    def test_age_is_int(self):
        """When checking age of tree it returns an int"""
        apple_tree = AppleTree()
        self.assertEqual(type(apple_tree.age), int)

    def test_height_is_int(self):
        """When checking height of tree it returns an int"""
        apple_tree = AppleTree()
        self.assertEqual(type(apple_tree.height), int)

    def test_age_tree(self):
        """When you age the tree, its age increases by 1"""
        apple_tree = AppleTree()
        self.assertEqual(apple_tree.age, 0)
        apple_tree.age_tree()
        self.assertEqual(apple_tree.age, 1)

    def test_age_tree_height(self):
        """When you age the tree, its height increases"""
        apple_tree = AppleTree()
        original_height = apple_tree.height
        self.assertEqual(original_height, 0)
        apple_tree.age_tree()
        self.assertGreater(apple_tree.height, original_height)
    
    def test_is_dead(self):
        """When you call the is_dead method, it lets you know if the tree is dead"""
        apple_tree = AppleTree()
        self.assertFalse(apple_tree.is_dead())
        apple_tree.age = 500
        self.assertTrue(apple_tree.is_dead())
    
    def test_any_apples(self):
        """When you call the any_apples method, it lets you know if there are any apples on the tree"""
        apple_tree = AppleTree()
        self.assertFalse(apple_tree.any_apples())
        for _ in itertools.repeat(None, 10):
            apple_tree.age_tree()
        self.assertTrue(apple_tree.any_apples())
    
    def test_pick_an_apple(self):
        """When you call the pick_an_apple method, it will return you an apple object"""
        apple_tree = AppleTree()
        apple = Apple(apple_tree.age)
        for _ in itertools.repeat(None, 10):
            apple_tree.age_tree()
        self.assertEqual(type(apple_tree.pick_an_apple()), type(apple))
    
    def test_pick_an_apple_error(self):
        """When you call the pick_an_apple method with a tree that has 0 apples, it will raise an error"""
        apple_tree = AppleTree()
        with self.assertRaises(Exception):
            apple_tree.pick_an_apple()

    def test_pick_apple_reduces_harvest(self):
        """When you call pick_an_apple method with a tree greater than 8 years old the harvest reduces by one"""
        apple_tree = AppleTree()
        for _ in itertools.repeat(None, 8):
            apple_tree.age_tree()
        original_harvest = apple_tree.harvest
        apple_tree.pick_an_apple()
        self.assertEqual(apple_tree.harvest, original_harvest -1 )

    def test_harvest(self):
        """Harvest should equal height times age once age is greater than 8 years old"""
        apple_tree = AppleTree()
        for _ in itertools.repeat(None, 8):
                apple_tree.age_tree()
        height_times_age = apple_tree.height * apple_tree.age
        self.assertEqual(apple_tree.harvest, height_times_age)

if __name__ == '__main__':
    unittest.main()
