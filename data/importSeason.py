from api import SQLiteAPI

league = 'bl2'
seasons = ['2011', '2012', '2013', '2014', '2015', '2016']


api = SQLiteAPI.SQLiteAPI()
for season in seasons:
    api.import_season(league, season)
