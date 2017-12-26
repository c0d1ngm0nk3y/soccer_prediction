#encoding=utf8
import unittest
from mock import MagicMock
import api.SQLiteAPI as SQLiteAPI


class SQLiteDataUnitTest(unittest.TestCase):
    def __init__(self, *args, **kwargs):
        super(SQLiteDataUnitTest, self).__init__(*args, **kwargs)
        self.api = None

    def setUp(self):
        self.api = SQLiteAPI.SQLiteAPI()
        self.api.conn = MagicMock()

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

    def test_import_data_one_game(self):
        game = self._create_game_data()
        data = [game]
        self.api._import_data('league', 'season', data)
