
from pig_latin import translate
import unittest

class TestPigLatin(unittest.TestCase):

    def test_apple(self):
        self.assertEqual(translate('apple'), 'appleay')

    def test_banana(self):
        self.assertEqual(translate('banana'), 'ananabay')

    def test_cherry(self):
        self.assertEqual(translate('cherry'), 'errychay')

    def test_eat_pie(self):
        self.assertEqual(translate('eat pie'), 'eatay iepay')

    def test_three(self):
        self.assertEqual(translate('three'), 'eethray')

    def test_school(self):
        self.assertEqual(translate('School'), 'Oolschay')

    def test_quiet(self):
        self.assertEqual(translate('Quiet'),'Ietquay')

    def test_square(self):
        self.assertEqual(translate('square'), 'aresquay')

    def test_many_words(self):
        self.assertEqual(translate('the quick brown fox'), 'ethay ickquay ownbray oxfay')


if __name__ == '__main__':
    unittest.main()