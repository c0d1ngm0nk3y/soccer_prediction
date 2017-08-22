import unittest
from prediction.Oracle import Oracle

class OracleTest(unittest.TestCase):
    def setUp(self):
        self.oracle = Oracle()

    def test_predict_game_day(self):

        result = self.oracle.predict_game_day('bl1', '2016', 30)

        self.assertIsNotNone(result)
        self.assertEqual(9, len(result))


if __name__ == '__main__':
    unittest.main()
