
import unittest
from caesar_cipher import caesar_cipher

class TestCeasarCipher(unittest.TestCase):

    def test_neg_five(self):
        self.assertEqual(caesar_cipher("Boy! What a string!", -5), "Wjt! Rcvo v nomdib!")

    def test_neg_five_again(self):
        self.assertEqual(caesar_cipher("Hello Zach168! Yes here.", -5), "Czggj Uvxc168! Tzn czmz.")

    def test_five(self):
        self.assertEqual(caesar_cipher("Hello zach168! Yes here.", 5), "Mjqqt efhm168! Djx mjwj.")

if __name__ == '__main__':
    unittest.main()