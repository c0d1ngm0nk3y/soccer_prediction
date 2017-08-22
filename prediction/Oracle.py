class PredictedResult(object):
    pass


class Oracle(object):
    def predict_game_day(self, league, season, game_day):
        result = []

        for i in range(0,9):
            result.append(PredictedResult())

        return result