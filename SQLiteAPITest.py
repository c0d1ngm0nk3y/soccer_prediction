import unittest
import SQLiteAPI


class MyTestCase(unittest.TestCase):
    def _test_insert_season_bl1_2016(self):
        api = SQLiteAPI.SQLiteAPI()
        api.import_season('bl1', '2016')

    def test_season_bl1_2016(self):
        api = SQLiteAPI.SQLiteAPI()
        table = api.get_game_table('bl1', '2016', 34)

        self.assertEquals(u'Bayern M\xfcnchen', table.get_name(1))
        self.assertEquals(82, table.get_points(1))
        self.assertEquals(3, table.get_position('Borussia Dortmund'))
        self.assertEquals(-35, table.get_goal_diff(18))
        self.assertEquals('Werder Bremen', table.get_name(8))
        self.assertEquals(45, table.get_points(8))
if __name__ == '__main__':
    unittest.main()
