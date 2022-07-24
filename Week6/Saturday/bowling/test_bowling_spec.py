import unittest
from classes.game import Game
from classes.frame import Frame
from classes.player import Player

class TestGame(unittest.TestCase):
    def setUp(self):
        self.game = Game()
        self.player1 = Player('Kevin')
        self.player2 = Player('Zella')


    def test_pins_after_roll(self):
        """Rolls a ball and pins should be less than or equal to when s"""
        frame = Frame()
        previous = frame.pins_remainding
        frame.roll()
        self.assertLessEqual(frame.pins_remainding, previous)

    def test_track_throws(self):
        """After each throw the throw variable increases by one"""
        frame = Frame()
        previous = frame.throw
        frame.roll()
        self.assertEqual(frame.throw, previous + 1)

    def test_strike(self):
        """ If first throw takes out all pins it is a strike"""
        frame = Frame()
        frame.throw = 1
        frame.pins_remainding = 0
        frame.check_condition(10)
        self.assertEqual(frame.gutter, False)
        self.assertEqual(frame.spare, False)
        self.assertEqual(frame.strike, True)

    def test_spare(self):
        """ If second throw takes out remainder of pins it is a spare"""
        frame = Frame()
        frame.throw = 2
        frame.pins_remainding = 0
        frame.check_condition(4)
        self.assertEqual(frame.gutter, False)
        self.assertEqual(frame.strike, False)
        self.assertEqual(frame.spare, True)

    def test_gutter(self):
        """ If throw takes out no pins it is a gutter ball"""
        frame = Frame()
        frame.throw = 1
        frame.pins = 10
        frame.check_condition(10)
        self.assertEqual(frame.strike, False)
        self.assertEqual(frame.strike, False)
        self.assertEqual(frame.gutter, True)

    def test_two_values_for_frame(self):
        """Play frame should return an array 2 elements long"""
        plyr = Player('Test')
        self.assertEqual(len(plyr.play_frame()), 2)

    def test_frame_in_frames(self):
        """Once a frame is played it should be added to frames"""
        plyr = Player('test')
        plyr.play_frame()
        self.assertIsInstance(plyr.frames[1], Frame)

    def test_multiple_frames(self):
        """ Checks that each frame gets added to frames"""
        plyr = Player('test')
        plyr.play_frame()
        plyr.play_frame()
        self.assertEqual(len(plyr.frames), 2)

    def test_simple_scoring_one_frame(self):
        """Scores one frame of 3, 4 to = 7"""
        plyr = Player('test')
        plyr.frames[1] = Frame()
        plyr.frames[1].score = [3,4]
        self.assertEqual(plyr.scoring(), 7)

    def test_simple_scoring_three_frames(self):
        """Scores 3 frames of 3, 4 to = 7 per frame and a score of 21"""
        plyr = Player('test')
        plyr.frames[1] = Frame()
        plyr.frames[1].score = [3,4]
        plyr.frames[2] = Frame()
        plyr.frames[2].score = [3,4]
        plyr.frames[3] = Frame()
        plyr.frames[3].score = [3,4]
        self.assertEqual(plyr.scoring(), 21)

    def test_scoring_strike(self):
        """Scores a strike with the next frame of 3, 4 and a score of 24"""
        plyr = Player('test')
        plyr.frames[1] = Frame()
        plyr.frames[1].score = [10,0]
        plyr.frames[1].strike = True
        plyr.frames[2] = Frame()
        plyr.frames[2].score = [3,4]
        plyr.current_frame = 2
        self.assertEqual(plyr.scoring(), 24)

    def test_scoring_one_frame_strike(self):
        """Scores one frame strike = 10"""
        plyr = Player('test')
        plyr.frames[1] = Frame()
        plyr.frames[1].score = [10, 0]
        plyr.frames[1].strike = True
        plyr.current_frame = 1
        self.assertEqual(plyr.scoring(), 10)

    def test_scoring_spare(self):
        """Scores a spare with the next frame of 3, 4 and a score of 20"""
        plyr = Player('test')
        plyr.frames[1] = Frame()
        plyr.frames[1].score = [1,9]
        plyr.frames[1].spare = True
        plyr.frames[2] = Frame()
        plyr.frames[2].score = [3,4]
        plyr.current_frame = 2
        self.assertEqual(plyr.scoring(), 20)

    def test_scoring_one_frame_spare(self):
        """Scores one frame spare = 10"""
        plyr = Player('test')
        plyr.frames[1] = Frame()
        plyr.frames[1].score = [1, 9]
        plyr.frames[1].spare = True
        plyr.current_frame = 1
        self.assertEqual(plyr.scoring(), 10)

if __name__ == '__main__':
    unittest.main()