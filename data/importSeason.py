from api import SQLiteAPI

league = 'bl1'
seasons = ['2008', '2007','2006']


api = SQLiteAPI.SQLiteAPI()
for season in seasons:
    api.import_season(league, season)
