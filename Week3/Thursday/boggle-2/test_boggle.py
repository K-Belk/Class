import unittest
from boggle_board import BoggleBoard

class TestBoggleBoard(unittest.TestCase):

    def setUp(self):
        self.board1 = BoggleBoard()
        self.board2 = BoggleBoard()

    def test_roll_dice_returns_random(self):
        self.assertNotEqual(self.board1.shake(), self.board2.shake(), "No way")


if __name__ == '__main__':
    unittest.main() 