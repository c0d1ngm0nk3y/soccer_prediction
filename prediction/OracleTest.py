from __future__ import absolute_import
import unittest
from prediction.Oracle import Oracle

class OracleTest(unittest.TestCase):
    def setUp(self):
        self.oracle = Oracle()

    def test_predict_game_day(self):

        result = self.oracle.predict_game_day('bl1', '2016', 30)

        self.assertIsNotNone(result)
        self.assertEqual(9, len(result))

        game = result[0]
        self.assertEqual(game.get_home_team(), u'1. FC K\xf6ln')
        self.assertEqual(game.get_away_team(), u'TSG 1899 Hoffenheim')


if __name__ == '__main__':
    unittest.main()
