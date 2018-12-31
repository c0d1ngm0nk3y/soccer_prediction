class NetProxy(object):
    def __init__(self, home, away):
        self.home = home
        self.away = away

    def query(self, input_list):
        home_result = self.home.query(input_list)
        away_result = self.away.query(input_list)
        return [home_result[0][0], away_result[0][0]]
