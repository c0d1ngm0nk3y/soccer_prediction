from api.OpenLigaDB import OpenLigaDB
from data.TestDataGenerator import TestDataGenerator
from prediction.NetTrainer import NetTrainer

class PredictedResult(object):
    def __init__(self, data):
        self.data = data
        self.prediction = None

    def get_home_team(self):
        return self.data['Team1']['TeamName']

    def get_away_team(self):
        return self.data['Team2']['TeamName']

    def get_prediction(self):
        return self.prediction

    def set_prediction(self, prediction):
        self.prediction = prediction

    def print_it(self):
        print('%25s : %25s  =>  %i' % (self.get_home_team(), self.get_away_team(), self.get_prediction()))

class Oracle(object):
    def __init__(self, net):
        self.net = net
        self.trainer = NetTrainer(net)
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
            prediction = self.trainer.interprete(v_out)
            day_prediction.set_prediction(prediction)

            result.append(day_prediction)

        return result

    def find_game_prediction(self, data, home_team):
        for x in data:
            day_prediction = PredictedResult(x)
            if day_prediction.get_home_team() == home_team:
                return day_prediction
        raise BaseException('game not found')
