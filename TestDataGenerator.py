from SQLiteAPI import SQLiteAPI

class TestDataGenerator(object):

    def __init__(self):
        self.api = SQLiteAPI()

    def generateFromSeason(self, league, season):
        data = []
        for i in range(5, 33):
            game_day = self.api.get_game_day(league, season, i)
            game_table = self.api.get_game_table(league, season, i)
            game_table_trend = self.api.get_game_table_trend(league, season, i)
            game_day_data = self.genererateFromGameDay(game_day, game_table, game_table_trend)
            data.extend(game_day_data)
        return data

    def extractInput(self, game_table, game_table_trend, team):
        pos = game_table.get_position(team)
        trend = game_table_trend.get_position(team)
        x_pos = self.get_input_for_position(pos)
        x_trend = self.get_input_for_position(trend)
        
        return (pos, trend, x_pos, x_trend)

    def genererateFromGameDay(self, game_day, game_table, game_table_trend):
        game_day_data = []
        for game in game_day:
            ht = game.get_home_team()
            hp = game.get_home_points()
            (pos_home, pos_home_trend, x_pos_home, x_pos_home_trend) = self.extractInput(game_table, game_table_trend, ht)

            at = game.get_away_team()
            ap = game.get_away_points()
            (pos_away, pos_away_trend, x_pos_away, x_pos_away_trend) = self.extractInput(game_table, game_table_trend, at)

            y_points_home = self.get_output_for_points(hp, ap)
            y_points_away = self.get_output_for_points(ap, hp)

            result = self.calculate_result(hp, ap)
            game_day_data.append(([x_pos_home, x_pos_away, x_pos_home_trend, x_pos_away_trend],[y_points_home, y_points_away],[result]))
        return game_day_data

    def get_input_for_position(self, position):
        input = max(((18 - position) / 17.0), 0.01)
        return round(input, 2)

    def get_output_for_points(self, x, y):
        diff = x - y
        out = 0.5 + (0.15 * diff)
        out = max(min(out, 0.99), 0.01)
        return out

    def calculate_result(self, home, away):
        if home > away:
            return 1
        if away > home:
            return 2
        return 0