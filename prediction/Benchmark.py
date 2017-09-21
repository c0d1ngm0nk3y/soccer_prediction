from prediction.NetTrainer import NetTrainer

class GameDayResult(object):
    def __init__(self, league, season, game_day, hits):
        self.league = league
        self.season = season
        self.game_day = game_day
        self.hits = hits

PAST_RESULTS = [GameDayResult('bl1', '2017', 3, 3),
                GameDayResult('bl1', '2017', 4, 5),
                GameDayResult('bl1', '2017', 5, 8),
                GameDayResult('bl2', '2017', 5, 3),
                GameDayResult('bl2', '2017', 6, 2),
                GameDayResult('bl2', '2017', 7, 4)]


def verify(net, factor=0.9):
    trainer = NetTrainer(net)
    expected = 0
    actual = 0

    for result in PAST_RESULTS:
        expected = expected + result.hits
        (_, actual_hits, _, _) = trainer.check_game_day(result.league,
                                                        result.season,
                                                        result.game_day)
        actual = actual + actual_hits

    verified = actual >= (expected * factor)
    #if not verified:
        #print actual, 'results correct, expected ', expected

    return verified
