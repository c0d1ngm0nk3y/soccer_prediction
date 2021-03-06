from api.SQLiteAPI import SQLiteAPI
from prediction.Judger import calculate_result_out_v_home_away

class TestDataInput(object):
    def __init__(self, x_pos, x_trend_points, x_home, x_goals):
        self.pos = x_pos
        self.trend_points = x_trend_points
        self.home = x_home
        self.goals = x_goals

    def fill_input(self, v_input):
        v_input.extend([self.pos, self.home])
        v_input.extend(self.trend_points)
        v_input.extend(self.goals)

class TestDataGenerator(object):

    SKIP_FIRST_N_GAME_DAYS = 4
    SKIP_LAST_N_GAME_DAYS = 2
    TOTAL_GAME_DAYS = 34

    def __init__(self, judger):
        self.api = SQLiteAPI()
        self.judger = judger

    def ignore_game_day(self, game_day, league, season):
        if game_day > self.TOTAL_GAME_DAYS - self.SKIP_LAST_N_GAME_DAYS:
            return True
        if game_day <= self.SKIP_FIRST_N_GAME_DAYS:
            return True
        first_game_day_after_break = self.api.select_first_after_break(league, season)
        after_break = game_day >= first_game_day_after_break
        not_into_season = game_day < first_game_day_after_break + self.SKIP_FIRST_N_GAME_DAYS
        if after_break and not_into_season:
            return True
        return False

    def generate_from_season(self, league, season):
        data = []
        for i in range(1, self.TOTAL_GAME_DAYS):
            if self.ignore_game_day(i, league, season):
                continue
            game_day_data = self.generate_from_game_gay(league, season, i)
            data.extend(game_day_data)
        return data

    def generate_from_game_gay(self, league, season, day):
        game_day_data = []
        game_day = self.api.get_game_day(league, season, day)

        prev_day = day - 1
        if prev_day == 0:
            prev_day = 34
            season = str(int(season) - 1)

        table = self.api.get_game_table(league, season, prev_day)
        table_trend4 = self.api.get_game_table_trend(league, season, prev_day, trend=4)
        table_trend3 = self.api.get_game_table_trend(league, season, prev_day, trend=3)
        table_trend2 = self.api.get_game_table_trend(league, season, prev_day, trend=2)
        table_trend1 = self.api.get_game_table_trend(league, season, prev_day, trend=1)
        trends = [table_trend1, table_trend2, table_trend3, table_trend4]
        table_home = self.api.get_game_table_home(league, season, prev_day)
        table_away = self.api.get_game_table_away(league, season, prev_day)

        for game in game_day:
            home_team = game.get_home_team()
            home_points = game.get_home_points()

            away_team = game.get_away_team()
            away_points = game.get_away_points()
            input_home = self.extract_input(table, trends, table_home, home_team)
            input_away = self.extract_input(table, trends, table_away, away_team)

            result = self.calculate_result(home_points, away_points)

            v_input = []
            input_home.fill_input(v_input)
            input_away.fill_input(v_input)
            output = self.judger.calculate_out_v(home_points, away_points)

            game_day_data.append((v_input, output, [result], game.get_home_team()))
        return game_day_data

    def extract_input(self, table, trend_tables, table_home, team):
        pos = table.get_position(team)
        x_pos = self.get_input_for_position(pos)

        relative_points = \
            [1.0*t.get_points(t.get_position(team))/t.get_points(1) for t in trend_tables]
        x_trend_points = list(map(self.get_input_for_relative_points, relative_points))

        home = table_home.get_position(team)
        x_home = self.get_input_for_position(home)
        offense = self.get_relative_table_property(team, table, 'offense')
        defense = self.get_relative_table_property(team, table, 'defense', reverse=True)
        x_goals = [offense, defense]

        return TestDataInput(x_pos, x_trend_points, x_home, x_goals)

    def get_relative_table_property(self, team, table, prop, reverse=False):
        _max = table.get_agg_property(max, prop)
        _min = table.get_agg_property(min, prop)

        x = table.get_property(team, prop)
        delta = max(x -_min, 0.1)
        delta_max = max(_max - _min, 0.1)
        value = 1.0 * delta / delta_max
        value = max(value, 0.01)
        if reverse:
            value = 1.01 - value
        return round(value, 2)

    def get_input_for_relative_points(self, fraction):
        x_input = max(fraction, 0.01)
        return round(x_input, 2)

    def get_input_for_position(self, position):
        x_input = max(((18 - position) / 17.0), 0.01)
        return round(x_input, 2)

    def calculate_result(self, home, away):
        if home > away:
            return 1
        if away > home:
            return 2
        return 0
