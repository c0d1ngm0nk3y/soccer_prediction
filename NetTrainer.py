from TestDataGenerator import TestDataGenerator

class PickLeader(object):
    def query(self, input_list):
        home = input_list[0]
        away = input_list[1]

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

    def train_season(self, league, season):
        season_data = self.generator.generateFromSeason(league, season)

        for data in season_data:
            (input, output, result) = data
            self.net.train(input, output)

    def check_season(self, league, season):
        season_data = self.generator.generateFromSeason(league, season)

        count = 0
        hits = 0
        for data in season_data:
            (input, output, result) = data
            result = result[0]
            query_output = self.net.query(input)
            query_result = self._interprete(query_output)

            count = count + 1
            if result == query_result:
                hits = hits + 1

            performance = self._get_performance(hits, count)

        return (performance, hits, count)

    def _get_performance(self, hits, count):
        percent = 100.0 * hits / count
        performance = int(percent)
        return performance

    def _interprete(self, out):
        home = out[0]
        away = out[1]
        threshold = 0.5

        if home > threshold and away < threshold:
            return 1
        if away > threshold and away < threshold:
            return 2
        return 0
