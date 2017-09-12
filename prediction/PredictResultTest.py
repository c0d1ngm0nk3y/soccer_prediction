from __future__ import absolute_import
import unittest
from prediction.Oracle import PredictedResult


class PredictResultTest(unittest.TestCase):

    def setUp(self):
        self.cut = PredictedResult([])

    def test_clear_home_win(self):
        self.cut.set_out([1, 0])

        self.assertEqual(self.cut.get_prediction(), 1)
        self.assertEqual(self.cut.get_confidence(), 99)

    def test_close_home_win(self):
        self.cut.set_out([0.6, 0.4])

        self.assertEqual(self.cut.get_prediction(), 1)
        self.assertEqual(self.cut.get_confidence(), 16)

    def test_clear_away_win(self):
        self.cut.set_out([0, 1])

        self.assertEqual(self.cut.get_prediction(), 2)
        self.assertEqual(self.cut.get_confidence(), 99)

    def test_close_away_win(self):
        self.cut.set_out([0.4, 0.65])

        self.assertEqual(self.cut.get_prediction(), 2)
        self.assertEqual(self.cut.get_confidence(), 21)

    def test_clear_draw(self):
        self.cut.set_out([0.5, 0.5])

        self.assertEqual(self.cut.get_prediction(), 0)
        self.assertEqual(self.cut.get_confidence(), 99)

    def test_close_draw(self):
        self.cut.set_out([0.48, 0.8])

        self.assertEqual(self.cut.get_prediction(), 0)
        self.assertEqual(self.cut.get_confidence(), 39)


if __name__ == '__main__':
    unittest.main()