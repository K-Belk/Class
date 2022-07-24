import unittest
from pad_array import pad

class TestPadArray(unittest.TestCase):

    def test_pad_None(self):
        self.assertEqual(pad([1,2,3], 5), [1,2,3,None,None])
    
    def test_min_less_than_length(self):
        self.assertEqual(pad([1,2,3,5,7], 3, 'tacos'), [1,2,3,5,7])

    def test_padding_with_strings(self):
        self.assertEqual(pad([1,2,3,5,7], 8, 'tacos'), [1,2,3,5,7, 'tacos', 'tacos', 'tacos'])

if __name__ == '__main__':
    unittest.main()