from data.TestDataGenerator import TestDataGenerator
from net.NeuralNetwork import NN2
from prediction.Judger import interprete, HomeAwayJudger
from prediction.QueryStatistics import QueryStatistics

def create_net(alpha=0.1
               , input_layer=16, hidden_layer=7, output_layer=2):
    net = NN2(input_layer, hidden_layer, output_layer, alpha)
    return net

def train_and_check(net, train_set=None, check='2017', train_leagues=None,
                    max_iterations=7, league='bl1', min_delta=0.2, trainer=None):
    if train_set is None:
        train_set = ['2013', '2014', '2015']
    if not train_leagues:
        train_leagues = [league]
    if not trainer:
        trainer = NetTrainer(net)
    error = 99999
    for _ in range(0, max_iterations):
        for a_league in train_leagues:
            prev_error = error
            error = trainer.train_seasons(a_league, train_set)
            delta = prev_error - error
            if delta < min_delta:
                return trainer.check_season(league, check)

    query_stats = trainer.check_season(league, check)
    return query_stats

class PickLeader(object):
    def query(self, input_list):
        home = input_list[0]
        away = input_list[len(input_list)/2]

        if home > away:
            return [0.99, 0.01]

        return [0.01, 0.99]

    def train(self, _input_list, _target_list):
        pass

class PickHome(object):
    def query(self, _input_list):
        return [0.99, 0.01]

    def train(self, _input_list, _target_list):
        pass

class PickAway(object):
    def query(self, _input_list):
        return [0.01, 0.99]

    def train(self, _input_list, _target_list):
        pass

class PickDraw(object):
    def query(self, _input_list):
        return [0.5, 0.5]

    def train(self, _input_list, _target_list):
        pass


class NetTrainer(object):

    def __init__(self, net, judger=None):
        self.net = net
        if not judger:
            judger = HomeAwayJudger()
        self.judger = judger
        self.generator = TestDataGenerator(judger)
        self.count = 0
        self.hits = 0
        self.statistics = [0, 0, 0]

    def train_seasons(self, league, seasons):
        train_data = []
        for season in seasons:
            season_data = self.generator.generate_from_season(league, season)
            train_data.extend(season_data)

        total_error = 0
        for data in train_data:
            (input_list, output_list, _, _) = data
            (_, errors) = self.net.train(input_list, output_list)
            single_error = 0
            for i in range(len(errors)):
                single_error = single_error + abs(errors[i][0])
            total_error = total_error + single_error

        return total_error

    def check_game_day(self, league, season, game_day):
        game_day_data = self.generator.generate_from_game_gay(league, season, game_day)
        return_code = self._check_data(game_day_data)
        return return_code

    def check_season(self, league, season):
        season_data = self.generator.generate_from_season(league, season)
        query_stats = self._check_data(season_data)
        return query_stats

    def _check_data(self, all_data):
        stats = QueryStatistics()
        for data in all_data:
            (input_list, _, result, _) = data
            result = result[0]
            query_output = self.net.query(input_list)
            query_result = self.judger.interprete(query_output)
            stats.add_result(result, query_result)
        return stats
