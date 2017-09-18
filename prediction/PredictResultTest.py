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
        self.cut.set_out([0.56, 0.44])

        self.assertEqual(self.cut.get_prediction(), 1)
        self.assertEqual(self.cut.get_confidence(), 51)

    def test_clear_away_win(self):
        self.cut.set_out([0, 1])

        self.assertEqual(self.cut.get_prediction(), 2)
        self.assertEqual(self.cut.get_confidence(), 99)

    def test_close_away_win(self):
        self.cut.set_out([0.44, 0.56])

        self.assertEqual(self.cut.get_prediction(), 2)
        self.assertEqual(self.cut.get_confidence(), 51)

    def test_clear_draw(self):
        self.cut.set_out([0.5, 0.5])

        self.assertEqual(self.cut.get_prediction(), 0)
        self.assertEqual(self.cut.get_confidence(), 99)

    def test_close_draw(self):
        self.cut.set_out([0.46, 0.8])

        self.assertEqual(self.cut.get_prediction(), 0)
        self.assertEqual(self.cut.get_confidence(), 0)


if __name__ == '__main__':
    unittest.main()
