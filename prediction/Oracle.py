from api.OpenLigaDB import OpenLigaDB

class PredictedResult(object):
    def __init__(self, data):
        self.data = data

    def get_home_team(self):
        return self.data['Team1']['TeamName']

    def get_away_team(self):
        return self.data['Team2']['TeamName']

    def print_it(self):
        print('%25s : %25s' % (self.get_home_team(), self.get_away_team()))

class Oracle(object):
    def predict_game_day(self, league, season, game_day):
        api = OpenLigaDB()
        data = api.request_data_game_day(league, season, game_day)
        result = []

        for x in data:
            result.append(PredictedResult(x))

        return result