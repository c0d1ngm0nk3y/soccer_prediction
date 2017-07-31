import unittest
import SQLiteAPI

class SQLiteDataTest(unittest.TestCase):
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

    def _test_insert_season_bl1_2015(self):
        api = SQLiteAPI.SQLiteAPI()
        api.import_season('bl1', '2015')

    def test_season_bl1_2015(self):
        api = SQLiteAPI.SQLiteAPI()
        table = api.get_game_table('bl1', '2015', 34)

        self.assertEquals(u'Bayern M\xfcnchen', table.get_name(1))
        self.assertEquals(88, table.get_points(1))

    def _test_insert_season_bl1_2014(self):
        api = SQLiteAPI.SQLiteAPI()
        api.import_season('bl1', '2014')

    def test_season_bl1_2014(self):
        api = SQLiteAPI.SQLiteAPI()
        table = api.get_game_table('bl1', '2014', 34)

        self.assertEquals(u'Bayern M\xfcnchen', table.get_name(1))
        self.assertEquals(u'VfL Wolfsburg', table.get_name(2))
        self.assertEquals(79, table.get_points(1))
        self.assertEquals(40, table.get_points(11))

    def _test_insert_season_bl1_2013(self):
        api = SQLiteAPI.SQLiteAPI()
        api.import_season('bl1', '2013')

    def test_season_bl1_2013_details(self):
        api = SQLiteAPI.SQLiteAPI()

        table = api.get_game_table('bl1', '2013', 2)
        self.assertEquals(6, table.get_points(1))

        table = api.get_game_table('bl1', '2013', 3)
        self.assertEquals('Borussia Dortmund', table.get_name(1))
        self.assertEquals(9, table.get_points(1))

        table = api.get_game_table('bl1', '2013', 5)
        self.assertEquals(15, table.get_points(1))

        table = api.get_game_table('bl1', '2013', 9)
        self.assertEquals(23, table.get_points(1))

        table = api.get_game_table('bl1', '2013', 18)
        self.assertEquals(50, table.get_points(1))

    def _test_insert_season_bl1_2012(self):
        api = SQLiteAPI.SQLiteAPI()
        api.import_season('bl1', '2012')

    def test_season_bl1_2012(self):
        api = SQLiteAPI.SQLiteAPI()

        table = api.get_game_table('bl1', '2012', 34)
        self.assertEquals(u'Bayern M\xfcnchen', table.get_name(1))
        self.assertEquals(91, table.get_points(1))
        self.assertEquals(21, table.get_points(18))
        self.assertEquals(u'SpVgg Greuther Fuerth', table.get_name(18))

    def test_season_bl1_2011(self):
        api = SQLiteAPI.SQLiteAPI()

        table = api.get_game_table('bl1', '2011', 34)
        self.assertEquals(u'Borussia Dortmund', table.get_name(1))
        self.assertEquals(81, table.get_points(1))

    def test_bl2(self):
        api = SQLiteAPI.SQLiteAPI()

        for season in ['2011', '2012', '2013', '2014', '2015', '2016']:
            table = api.get_game_table('bl2', season, 34)
            self.assertGreater(table.get_points(1), 63)

    def test_get_game_day(self):
        api = SQLiteAPI.SQLiteAPI()
        data = api.get_game_day('bl1', '2014', 1)

        self.assertEqual(9, len(data))
        game = data[0]
        self.assertIsNotNone(game.get_home_team())
        self.assertIsNotNone(game.get_home_points())
        self.assertIsNotNone(game.get_away_team())
        self.assertIsNotNone(game.get_away_points())

    def test_game_table_trend(self):
        api = SQLiteAPI.SQLiteAPI()

        table = api.get_game_table_trend('bl1', '2015', 32)
        self.assertEquals(u'Borussia Dortmund', table.get_name(1))
        self.assertEquals(9, table.get_points(1))
        self.assertEquals(0, table.get_points(18))
        self.assertEquals(u'VfB Stuttgart', table.get_name(18))

    def test_game_table_home(self):
        api = SQLiteAPI.SQLiteAPI()

        table = api.get_game_table_home('bl1', '2016', 34)
        self.assertEquals(u'Borussia Dortmund', table.get_name(2))
        self.assertEquals(43, table.get_points(2))
        self.assertEquals(17, table.get_points(18))
        self.assertEquals(u'FC Ingolstadt 04', table.get_name(18))

    def test_game_table_away(self):
        api = SQLiteAPI.SQLiteAPI()

        table = api.get_game_table_away('bl1', '2016', 33)
        self.assertEquals(u'RB Leipzig', table.get_name(2))
        self.assertEquals(28, table.get_points(2))
        self.assertEquals(3, table.get_points(18))
        self.assertEquals(u'SV Darmstadt 98', table.get_name(18))


if __name__ == '__main__':
    unittest.main()
