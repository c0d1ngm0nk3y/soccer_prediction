#encoding=utf8
import unittest
from mock import MagicMock
import api.SQLiteAPI as SQLiteAPI


class SQLiteDataUnitTest(unittest.TestCase):
    def __init__(self, *args, **kwargs):
        super(SQLiteDataUnitTest, self).__init__(*args, **kwargs)
        self.api = None
        self.cursor = None

    def setUp(self):
        self.api = SQLiteAPI.SQLiteAPI()
        self.api.conn = MagicMock()
        self.cursor = MagicMock()
        self.api.conn.cursor.return_value = self.cursor

    def _create_result_data(self):
        result = {}
        return result

    def _create_team_data(self, name):
        team = {'TeamName': name}
        return team

    def _create_game_data(self, match_id=1, game_day=1):
        game = {'Group': {'GroupOrderID': game_day}, 'MatchID': match_id}
        game['Team1'] = self._create_team_data('Team A')
        game['Team2'] = self._create_team_data('Team B')
        game['MatchResults'] = self._create_result_data()
        return game

    def test_import_data_empty(self):
        data = []
        self.api._import_data('league', 'season', data)
        self.assertEquals(self.cursor.execute.call_count, 0)

    def test_import_data_one_game(self):
        game = self._create_game_data()
        data = [game]
        self.api._import_data('league', 'season', data)
        self.assertEquals(self.cursor.execute.call_count, 2)

    def test_import_data_two_games(self):
        game1 = self._create_game_data(match_id=1)
        game2 = self._create_game_data(match_id=2)
        data = [game1, game2]
        self.api._import_data('league', 'season', data)
        self.assertEquals(self.cursor.execute.call_count, 4)

    def test_import_data_debug(self):
        game = self._create_game_data()
        data = [game]
        self.api._import_data('league', 'season', data, debug=True)
        self.assertEquals(self.cursor.execute.call_count, 0)

    def test_points_home(self):
        points = self.api.calculate_points(2, 1)
        self.assertEquals(points, 3)

    def test_points_away(self):
        points = self.api.calculate_points(1, 5)
        self.assertEquals(points, 0)

    def test_points_deuce(self):
        points = self.api.calculate_points(0, 0)
        self.assertEquals(points, 1)
