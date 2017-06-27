import requests

class OpenLigaDB(object):

    def request_data(self, league, season):
        url = 'https://www.openligadb.de/api/getmatchdata/{0}/{1}'.format(league, season)
        r = requests.get(url)
        data = r.json()
        return data
