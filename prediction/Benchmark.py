import logging
from prediction.NetTrainer import NetTrainer, train_and_check
from prediction.Serializer import load_net


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
                        GameDayResult('bl1', '2017', 31, 5)

                                              ],

                'bl2': [GameDayResult('bl2', '2017', 5, 3),
                        GameDayResult('bl2', '2017', 6, 2),
                        GameDayResult('bl2', '2017', 7, 4)
                       ]}


def verify(net, league='bl1', factor=1.0, delta=0):
    logger = logging.getLogger()
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

    return verified

def load_and_check(filename):
    logger = logging.getLogger()
    net = load_net(filename)

    result = train_and_check(net, train_set=[])
    logger.debug('using file %s', filename)
    logger.info(result)
    verify(net)
    return net
