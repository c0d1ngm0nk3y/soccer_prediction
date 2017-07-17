from SQLiteAPI import SQLiteAPI

class TestDataGenerator(object):

    def __init__(self):
        self.api = SQLiteAPI()

    def generateFromSeason(self, league, season):
        data = []
        for i in range(5, 33):
            game_day = self.api.get_game_day(league, season, i)
            game_table = self.api.get_game_table(league, season, i)
            game_day_data = self.genererateFromGameDay(game_day, game_table)
            data.extend(game_day_data)
        return data

    def genererateFromGameDay(self, game_day, game_table):
        game_day_data = []
        for game in game_day:
            ht = game.get_home_team()
            hp = game.get_home_points()
            pos_home = game_table.get_position(ht)
            x_pos_home = self.get_input_for_position(pos_home)
            at = game.get_away_team()
            ap = game.get_away_points()
            pos_away = game_table.get_position(at)
            x_pos_away = self.get_input_for_position(pos_away)


            y_points_home = self.get_output_for_points(hp, ap)
            y_points_away = self.get_output_for_points(ap, hp)

            result = self.calculate_result(hp, ap)
            game_day_data.append(([x_pos_home, x_pos_away],[y_points_home, y_points_away],[result]))
        return game_day_data

    def get_input_for_position(self, position):
        return max(((18 - position) / 17), 0.01)

    def get_output_for_points(self, x, y):
        return 0.99 if x > y else 0.01

    def calculate_result(self, home, away):
        if home > away:
            return 1
        if away > home:
            return 2
        return 0