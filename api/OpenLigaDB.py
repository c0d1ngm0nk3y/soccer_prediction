import requests

class OpenLigaDB(object):

    def request_data(self, league, season):
        url = 'https://www.openligadb.de/api/getmatchdata/{0}/{1}'.format(league, season)
        r = requests.get(url)
        data = r.json()
        return data


    def request_data_game_day(self, league, season, game_day):
        url = 'https://www.openligadb.de/api/getmatchdata/{0}/{1}/{2}'.format(league, season, game_day)
        r = requests.get(url)
        data = r.json()
        return data
