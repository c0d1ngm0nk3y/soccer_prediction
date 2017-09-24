from api.SQLiteAPI import SQLiteAPI
from prediction.judger.DrawDiff import calculate_output_for_points

class TestDataInput(object):
    def __init__(self, x_pos, x_trend_points, x_home, x_goals):
        self.pos = x_pos
        self.trend_points = x_trend_points
        self.home = x_home
        self.goals = x_goals

    def fill_input(self, input):
        input.extend([self.pos, self.home])
        input.extend(self.trend_points)
        input.extend(self.goals)

class TestDataGenerator(object):

    def __init__(self):
        self.api = SQLiteAPI()

    def generateFromSeason(self, league, season):
        data = []
        for i in range(5, 33):
            game_day_data = self.genererateFromGameDay(league, season, i)
            data.extend(game_day_data)
        return data

    def genererateFromGameDay(self, league, season, day):
        game_day_data = []
        game_day = self.api.get_game_day(league, season, day)

        state = day - 1
        table = self.api.get_game_table(league, season, state)
        table_trend4 = self.api.get_game_table_trend(league, season, state, trend=4)
        table_trend3 = self.api.get_game_table_trend(league, season, state, trend=3)
        table_trend2 = self.api.get_game_table_trend(league, season, state, trend=2)
        table_trend1 = self.api.get_game_table_trend(league, season, state, trend=1)
        trends = [table_trend1, table_trend2, table_trend3, table_trend4]
        table_home = self.api.get_game_table_home(league, season, state)
        table_away = self.api.get_game_table_away(league, season, state)

        for game in game_day:
            ht = game.get_home_team()
            hp = game.get_home_points()
            input_home = self.extractInput(table, trends, table_home, ht)

            at = game.get_away_team()
            ap = game.get_away_points()
            input_away = self.extractInput(table, trends, table_away, at)

            y_points_home = calculate_output_for_points(hp, ap)
            y_points_away = calculate_output_for_points(ap, hp)

            result = self.calculate_result(hp, ap)

            input = []
            input_home.fill_input(input)
            input_away.fill_input(input)

            output = [y_points_home, y_points_away]
            game_day_data.append((input, output, [result], game.get_home_team()))
        return game_day_data

    def extractInput(self, table, trend_tables, table_home, team):
        pos = table.get_position(team)
        x_pos = self.get_input_for_position(pos)

        relative_points = list(map(lambda t: 1.0*t.get_points(t.get_position(team))/t.get_points(1), trend_tables))
        x_trend_points = list(map(lambda rp: self.get_input_for_relative_points(rp), relative_points))

        home = table_home.get_position(team)
        x_home = self.get_input_for_position(home)
        offense = self.get_relative_table_property(team, table, 'offense')
        defense = self.get_relative_table_property(team, table, 'defense')
        x_goals = [offense, defense]

        return TestDataInput(x_pos, x_trend_points, x_home, x_goals)

    def get_relative_table_property(self, team, table, property):
        _max = table.get_agg_property(max, property)
        _min = table.get_agg_property(min, property)

        x = table.get_property(team, property)
        delta = max(x -_min, 0.1)
        delta_max = max(_max - _min, 0.1)
        value = 1.0 * delta / delta_max
        return max(round(value, 2), 0.01)

    def get_input_for_relative_points(self, fraction):
        input = max(fraction, 0.01)
        return round(input, 2)

    def get_input_for_position(self, position):
        input = max(((18 - position) / 17.0), 0.01)
        return round(input, 2)

    def calculate_result(self, home, away):
        if home > away:
            return 1
        if away > home:
            return 2
        return 0