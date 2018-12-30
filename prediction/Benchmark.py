import logging
from prediction.NetTrainer import NetTrainer, train_and_check
from prediction.Serializer import load_net
from prediction.Judger import create_judger

class NetEntry(object):
    def __init__(self, path, points, verify_results, stats):
        self.path = path
        self.points = points
        self.verify = verify_results
        self.stats = stats

    def __str__(self):
        return '{0} points: {1} ({2}, {3})'.format(self.points, self.path, self.verify, self.stats)

class GameDayResult(object):
    def __init__(self, league, season, game_day, hits):
        self.league = league
        self.season = season
        self.game_day = game_day
        self.hits = hits


PAST_RESULTS = {'bl1': [GameDayResult('bl1', '2017', 3, 3),
                        GameDayResult('bl1', '2017', 4, 5),
                        GameDayResult('bl1', '2017', 5, 8),
                        GameDayResult('bl1', '2017', 6, 5),
                        GameDayResult('bl1', '2017', 7, 4),
                        GameDayResult('bl1', '2017', 8, 4),
                        GameDayResult('bl1', '2017', 9, 4),
                        GameDayResult('bl1', '2017', 10, 6),
                        GameDayResult('bl1', '2017', 11, 6),
                        GameDayResult('bl1', '2017', 12, 4),
                        GameDayResult('bl1', '2017', 13, 3),
                        GameDayResult('bl1', '2017', 14, 2),
                        GameDayResult('bl1', '2017', 15, 2),
                        GameDayResult('bl1', '2017', 16, 7),
                        GameDayResult('bl1', '2017', 17, 5),
                        GameDayResult('bl1', '2017', 18, 3),
                        GameDayResult('bl1', '2017', 19, 2),
                        GameDayResult('bl1', '2017', 20, 3),
                        GameDayResult('bl1', '2017', 21, 3),
                        GameDayResult('bl1', '2017', 22, 7),
                        GameDayResult('bl1', '2017', 23, 4),
                        GameDayResult('bl1', '2017', 24, 2),
                        GameDayResult('bl1', '2017', 25, 7),
                        GameDayResult('bl1', '2017', 26, 6),
                        GameDayResult('bl1', '2017', 27, 6),
                        GameDayResult('bl1', '2017', 28, 4),
                        GameDayResult('bl1', '2017', 29, 3),
                        GameDayResult('bl1', '2017', 30, 7),
                        GameDayResult('bl1', '2017', 31, 5),
                        GameDayResult('bl1', '2017', 32, 3),
                        GameDayResult('bl1', '2017', 33, 6),
                        GameDayResult('bl1', '2017', 34, 3),
                        GameDayResult('bl1', '2018', 1, 6),
                        GameDayResult('bl1', '2018', 2, 3),
                        GameDayResult('bl1', '2018', 3, 6),
                        GameDayResult('bl1', '2018', 4, 3),
                        GameDayResult('bl1', '2018', 5, 5),
                        GameDayResult('bl1', '2018', 6, 3),
                        GameDayResult('bl1', '2018', 7, 4),
                        GameDayResult('bl1', '2018', 8, 4),
                        GameDayResult('bl1', '2018', 9, 1),
                        GameDayResult('bl1', '2018', 10, 4),
                        GameDayResult('bl1', '2018', 11, 5),
                        GameDayResult('bl1', '2018', 12, 5),
                        GameDayResult('bl1', '2018', 13, 2),
                        GameDayResult('bl1', '2018', 14, 7),
                        GameDayResult('bl1', '2018', 15, 4),
                        GameDayResult('bl1', '2018', 16, 3),
                        GameDayResult('bl1', '2018', 17, 3)
                                                 ],

                'bl2': [GameDayResult('bl2', '2017', 5, 3),
                        GameDayResult('bl2', '2017', 6, 2),
                        GameDayResult('bl2', '2017', 7, 4)
                       ]}


def verify(net, league='bl1', factor=1.0, delta=0, trainer=None):
    logger = logging.getLogger()
    if not trainer:
        trainer = NetTrainer(net)
    expected = 0
    actual = 0

    for result in PAST_RESULTS[league]:
        expected = expected + result.hits
        results = trainer.check_game_day(result.league,
                                         result.season,
                                         result.game_day)
        actual = actual + results.get_hits()

    verified = actual >= min((expected * factor), (expected - delta))
    logger.debug('verify: %d / %d -> %s', actual, expected, verified)

    return (verified, (actual - expected))


def load_and_check(filename, league, _type):
    logger = logging.getLogger()
    net = load_net(filename)
    trainer = NetTrainer(net, create_judger(_type))

    query_stats = train_and_check(net, train_set=[], trainer=trainer)
    logger.debug('using file %s', filename)
    logger.debug(query_stats)
    (_, verify_result) = verify(net, league=league, trainer=trainer)
    points = calculate_points(query_stats, verify_result)
    entry = NetEntry(filename, points, verify_result, query_stats)
    return (net, entry)

def calculate_points(stats, verify_result):
    performance_points = stats.get_performance() * 2
    expected_points = stats.get_expected_win_ratio() * 50
    return performance_points + expected_points + verify_result
