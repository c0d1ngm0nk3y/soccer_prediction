from api.OpenLigaDB import OpenLigaDB
from data.TestDataGenerator import TestDataGenerator
from prediction.NetTrainer import NetTrainer
from api.SQLiteAPI import SQLiteAPI

class PredictedResult(object):
    def __init__(self, data):
        self.data = data
        self.prediction = None
        self.trainer = NetTrainer(None)
        self.api = SQLiteAPI()
        self.game = self.api.get_result(self.data)
        self.v_in = None
        self.v_out = None

    def get_home_team(self):
        return self.data['Team1']['TeamName']

    def get_away_team(self):
        return self.data['Team2']['TeamName']

    def get_home_points(self):
        return int(self.game['PointsTeam1'])

    def get_away_points(self):
        return int(self.game['PointsTeam2'])

    def get_predicted_home_points(self):
        prediction = self.get_prediction()
        if prediction == 1:
            return 1
        else:
            return 0

    def get_predicted_away_points(self):
        prediction = self.get_prediction()
        if prediction == 2:
            return 1
        else:
            return 0

    def get_prediction(self):
        prediction = self.trainer.interprete(self.v_out)
        return prediction

    def set_in(self, v_in):
        self.v_in = v_in

    def set_out(self, v_out):
        self.v_out = v_out

    def print_it(self, debug = False):
        print('%25s : %25s  =>  %i (%i:%i) / %i:%i'
              % (self.get_home_team(), self.get_away_team(), self.get_prediction(),
                 self.get_predicted_home_points(), self.get_predicted_away_points(),
                 self.get_home_points(), self.get_away_points()))
        if debug:
            print self.v_in, '=>', self.v_out[0], self.v_out[1]

class Oracle(object):
    def __init__(self, net):
        self.net = net
        self.api = OpenLigaDB()
        self.generator = TestDataGenerator()

    def predict_game_day(self, league, season, game_day):
        data = self.api.request_data_game_day(league, season, game_day)

        test_data = self.generator.genererateFromGameDay(league, season, game_day)
        result = []

        for i in range(len(data)):
            (v_in, _, _, home_team) = test_data[i]
            day_prediction = self.find_game_prediction(data, home_team)

            v_out = self.net.query(v_in)
            day_prediction.set_in(v_in)
            day_prediction.set_out(v_out)

            result.append(day_prediction)

        return result

    def find_game_prediction(self, data, home_team):
        for x in data:
            day_prediction = PredictedResult(x)
            if day_prediction.get_home_team() == home_team:
                return day_prediction
        raise BaseException('game not found')
