#encoding=utf8
from __future__ import absolute_import
import unittest
from prediction.Oracle import Oracle
from prediction.NetTrainer import PickHome

class OracleTest(unittest.TestCase):
    def setUp(self):
        net = PickHome()
        self.oracle = Oracle(net)

    def test_predict_game_day(self):

        result = self.oracle.predict_game_day('bl1', '2016', 30)

        self.assertIsNotNone(result)
        self.assertEqual(9, len(result))

        game = result[0]
        self.assertEqual(game.get_home_team(), '1. FC Köln')
        self.assertEqual(game.get_away_team(), u'TSG 1899 Hoffenheim')
        self.assertEqual(game.get_prediction(), 1)


if __name__ == '__main__':
    unittest.main()
