EXPECTED_WIN = [3.25, 1.75, 2.25]

class QueryStatistics(object):
    def __init__(self):
        self.count = 0
        self.hits = 0
        self.statistics = [0, 0, 0]
        self.win = 0

    def add_result(self, expected, actual):
        self.count = self.count + 1
        if expected == actual:
            self.hits = self.hits + 1
            self.statistics[actual] = self.statistics[actual] + 1
            self.win = self.win + EXPECTED_WIN[expected]

    def get_performance(self):
        if not self.count:
            return 0

        percent = 100.0 * self.hits / self.count
        performance = int(percent)
        return performance

    def get_count(self):
        return self.count

    def get_hits(self):
        return self.hits

    def get_statistics(self):
        return self.statistics

    def get_expected_win_ratio(self):
        if not self.count:
            return 0

        return round(1.0 * self.win / self.count, 2)

    def __str__(self):
        return '{0}% ({1}, {2}, {3}) {4}'.format(self.get_performance(),
                                                  self.statistics[0],
                                                  self.statistics[1],
                                                  self.statistics[2],
                                                  self.get_expected_win_ratio())
