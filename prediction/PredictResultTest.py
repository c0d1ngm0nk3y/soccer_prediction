from __future__ import absolute_import
import unittest
from prediction.Oracle import PredictedResult

def create_result(home, away):
    return {'ResultName': 'Endergebnis',
            'PointsTeam1': home,
            'PointsTeam2': away}

class PredictResultTest(unittest.TestCase):

    def setUp(self):
        self.cut = PredictedResult({})

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

    def test_actual_result_home(self):
        self.cut = PredictedResult({'MatchResults': [create_result(2, 1)]})
        self.assertEqual(self.cut.get_actual_result(), 1)

    def test_actual_result_away(self):
        self.cut = PredictedResult({'MatchResults': [create_result(1, 2)]})
        self.assertEqual(self.cut.get_actual_result(), 2)

    def test_actual_result_draw(self):
        self.cut = PredictedResult({'MatchResults': [create_result(0, 0)]})
        self.assertEqual(self.cut.get_actual_result(), 0)

    def test_predicted_home_points(self):
        self.cut.set_out([0.99, 0.1])
        self.assertEqual(self.cut.get_predicted_home_points(), 1)

    def test_predicted_away_points(self):
        self.cut.set_out([0.1, 0.99])
        self.assertEqual(self.cut.get_predicted_away_points(), 1)

    def test_predicted_draw_points(self):
        self.cut.set_out([0.5, 0.5])
        self.assertEqual(self.cut.get_predicted_home_points(), self.cut.get_predicted_away_points())

    def test_prediction_marker_x_home(self):
        self.cut = PredictedResult({'MatchResults': [create_result(2, 1)]})
        self.cut.set_out([0.9, 0.1])
        self.assertEqual(self.cut.get_correct_prediction_marker(), 'X')

    def test_prediction_marker_x_away(self):
        self.cut = PredictedResult({'MatchResults': [create_result(1, 2)]})
        self.cut.set_out([0.2, 0.8])
        self.assertEqual(self.cut.get_correct_prediction_marker(), 'X')

    def test_prediction_marker___draw(self):
        self.cut = PredictedResult({'MatchResults': [create_result(1, 1)]})
        self.cut.set_out([0.6, 0.4])
        self.assertEqual(self.cut.get_correct_prediction_marker(), '')


if __name__ == '__main__':
    unittest.main()
