from data.TestDataGenerator import TestDataGenerator
from NeuralNetwork import NN2

def create_net(alpha=0.1, input=16, hidden=8, output=2):
    net = NN2(input, hidden, output, alpha)
    return net

def train_and_check(net, train_set, check, iterations = 25, league='bl1'):
    trainer = NetTrainer(net)
    for i in range(0, iterations):
        for train in train_set:
            trainer.train_season(league, train)
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


class NetTrainer(object):

    def __init__(self, net):
        self.net = net
        self.generator = TestDataGenerator()
        self.count = 0
        self.hits = 0
        self.statistics = [0, 0, 0]

    def train_season(self, league, season):
        season_data = self.generator.generateFromSeason(league, season)

        for data in season_data:
            (input, output, result, _) = data
            self.net.train(input, output)

    def check_season(self, league, season):
        season_data = self.generator.generateFromSeason(league, season)

        self._reset_statistics()
        for data in season_data:
            (input, output, result, _) = data
            result = result[0]
            query_output = self.net.query(input)
            query_result = self.interprete(query_output)
            #if result == 0:
                #print query_result, query_output

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
        home = out[0]
        away = out[1]
        threshold = 0.5
        variable = 0.05

        if home > (threshold + variable) and away < (threshold - variable):
            return 1
        if away > (threshold + variable) and home < (threshold - variable):
            return 2
        return 0
