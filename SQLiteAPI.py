import sqlite3
import OpenLigaDB

class Game(object):
    def __init__(self, data):
        self.data = data

    def print_data(self):
        for x in self.data:
            print(x)

    def get_home_team(self):
        return self.data[0]

    def get_home_points(self):
        return self.data[1]

    def get_away_team(self):
        return self.data[2]

    def get_away_points(self):
        return self.data[3]


class GameTable(object):
    def __init__(self, data):
        self.data = data

    def get_name(self, position):
        (name, _, _) = self.data[position-1]
        return name

    def get_points(self, position):
        (_, points, _) = self.data[position-1]
        return points

    def get_position(self, name):
        for i in range(1, len(self.data)+1):
            n = self.get_name(i)
            if n == name:
                return i
        return -1

    def get_goal_diff(self, position):
        (_, _, diff) = self.data[position - 1]
        return diff

    def print_data(self):
        for x in self.data:
            print(x)


class SQLiteAPI(object):
    def __init__(self):
        self.api = OpenLigaDB.OpenLigaDB()
        self.conn = None

    def import_season(self, league, season, debug=False):
        self.conn = sqlite3.connect('games.sqlite')

        data = self.api.request_data(league, season)

        for game in data:
            if debug:
                print(game)
            game_day = game['Group']['GroupOrderID']
            match = game['MatchID']

            team = self.get_name(game['Team1'])
            home = 1
            goals_own = self.get_result(game)['PointsTeam1']
            goals_opponent = self.get_result(game)['PointsTeam2']
            points = self.calculate_points(goals_own, goals_opponent)
            if not debug:
                self.insert_game(league, season, game_day, team, home, goals_own, goals_opponent, points, match)

            team = self.get_name(game['Team2'])
            home = 0
            goals_own = self.get_result(game)['PointsTeam2']
            goals_opponent = self.get_result(game)['PointsTeam1']
            points = self.calculate_points(goals_own, goals_opponent)
            if not debug:
                self.insert_game(league, season, game_day, team, home, goals_own, goals_opponent, points, match)

        self.conn.commit()
        self.conn.close()

    def get_result(self, game):
        for result in game['MatchResults']:
            if result['ResultName'] == 'Endergebnis':
                return result
        raise Exception()

    def calculate_points(self, goals1, goals2):
        if goals1 > goals2:
            return 3
        if goals2 > goals1:
            return 0
        return 1

    def get_name(self, team):
        return team['TeamName']

    def insert_game(self, league, season, game_day, team, home, goals_own, goals_opponent, points, match):
        c = self.conn.cursor()
        c.execute(u"INSERT INTO results VALUES('{0}', '{1}', {2}, '{3}', {4}, {5}, {6}, {7}, {8})"
                  .format(league, season, game_day, team, home, goals_own, goals_opponent, points, match))

    def get_game_table(self, league, season, game_day):
        table = self.get_game_table_generic(league, season, game_day, "1 =", 1)
        return table

    def get_game_table_trend(self, league, season, game_day, trend=2):
        table = self.get_game_table_generic(league, season, game_day, "game_day >=", (game_day - trend))
        return table

    def get_game_table_home(self, league, season, game_day):
        table = self.get_game_table_generic(league, season, game_day, "home =", 1)
        return table

    def get_game_table_away(self, league, season, game_day):
        table = self.get_game_table_generic(league, season, game_day, "home =", 0)
        return table

    def get_game_table_generic(self, league, season, game_day, additional_prop, binding):
        self.conn = sqlite3.connect('games.sqlite')
        c = self.conn.cursor()
        data = c.execute("SELECT team, SUM(points), SUM(goals_own - goals_opponent)"
                         "FROM results "
                         "WHERE league = ? and season = ? and game_day <= ? and {0} ? "
                         ""
                         "GROUP BY team "
                         "ORDER BY 2 DESC, 3 DESC".format(additional_prop),
                         [league, season, game_day, binding]).fetchall()
        self.conn.close()

        return GameTable(data)

    def get_game_day(self, league, season, game_day):
        games = []
        self.conn = sqlite3.connect('games.sqlite')
        c = self.conn.cursor()
        data = c.execute("SELECT home.team, home.goals_own, away.team, away.goals_own "
                         "FROM results home "
                         "INNER JOIN "
                         "results away "
                         "ON home.match = away.match "
                         "WHERE home.league = ? and home.season = ? and home.game_day = ? "
                         "AND away.league = ? and away.season = ? and away.game_day = ? "
                         "AND home.home = 1 "
                         "AND away.home = 0 ",
                         [league, season, game_day, league, season, game_day]).fetchall()

        for row in data:
            games.append(Game(row))

        self.conn.close()
        return games
