from SQLiteAPI import SQLiteAPI

class TestDataGenerator(object):

    def __init__(self):
        self.api = SQLiteAPI()

    def generateFromSeason(self, league, season):
        data = []
        for i in range(5, 33):
            game_day = self.api.get_game_day(league, season, i)
            game_day_data = self.genererateFromGameDay(game_day)
            data.extend(game_day_data)
        return data

    def genererateFromGameDay(self, game_day):
        game_day_data = []
        for x in game_day:
            game_day_data.append(([],[]))
        return game_day_data