from api import SQLiteAPI

league = 'bl1'
seasons = ['2010', '2009']


api = SQLiteAPI.SQLiteAPI()
for season in seasons:
    api.import_season(league, season)
