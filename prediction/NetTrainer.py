from data.TestDataGenerator import TestDataGenerator
from NeuralNetwork import NN2
from prediction.Util import calculate_confidence, interprete

def create_net(alpha=0.05, input=16, hidden=14, output=2):
    net = NN2(input, hidden, output, alpha)
    return net

def train_and_check(net, train_set=['2013', '2014', '2015'], check='2016', max_iterations = 10, league='bl1', min_delta=0.2):
    trainer = NetTrainer(net)
    error = 999
    for i in range(0, max_iterations):
        prev_error = error
        error = trainer.train_seasons(league, train_set)
        delta = prev_error - error
        #print 'iteration', i + 1, 'error:', error, 'delta:', delta
        if delta < min_delta:
            break

    tuple = trainer.check_season(league, check)
    return tuple

class PickLeader(object):
    def query(self, input_list):
        home = input_list[0]
        away = input_list[len(input_list)/2]

        if home > away:
            return [0.99, 0.01]
        else:
            return [0.01, 0.99]

    def train(self, input_list, target_list):
        pass


class PickHome(object):
    def query(self, input_list):
        return [0.99, 0.01]

    def train(self, input_list, target_list):
        pass

class PickAway(object):
    def query(self, input_list):
        return [0.01, 0.99]

    def train(self, input_list, target_list):
        pass


class NetTrainer(object):

    def __init__(self, net):
        self.net = net
        self.generator = TestDataGenerator()
        self.count = 0
        self.hits = 0
        self.statistics = [0, 0, 0]

    def train_seasons(self, league, seasons):
        train_data = []
        for season in seasons:
            season_data = self.generator.generateFromSeason(league, season)
            train_data.extend(season_data)

        total_error = 0
        for data in train_data:
            (input, output, result, _) = data
            (_, errors) = self.net.train(input, output)
            single_error = abs(errors[0][0]) + abs(errors[1][0])
            total_error = total_error + single_error

        return total_error

    def check_game_day(self, league, season, game_day):
        game_day_data = self.generator.genererateFromGameDay(league, season, game_day)
        rc = self._check_data(game_day_data)
        return rc

    def check_season(self, league, season):
        season_data = self.generator.generateFromSeason(league, season)
        rc = self._check_data(season_data)
        return rc

    def _check_data(self, all_data):
        self._reset_statistics()
        for data in all_data:
            (input, output, result, _) = data
            result = result[0]
            query_output = self.net.query(input)
            query_result = self.interprete(query_output)
            self._update_statistics(result, query_result)
        rc = self._get_result()
        return rc

    def _reset_statistics(self):
        self.count = 0
        self.hits = 0
        self.statistics = [0, 0, 0]

    def _update_statistics(self, expected, actual):
        self.count = self.count + 1
        if expected == actual:
            self.hits = self.hits + 1
            self.statistics[actual] = self.statistics[actual] + 1

    def _get_result(self):
        percent = 100.0 * self.hits / self.count
        performance = int(percent)
        return (performance, self.hits, self.count, self.statistics)

    def interprete(self, out):
        return interprete(out)

    def calculate_confidence(self, out):
        return calculate_confidence(out)
