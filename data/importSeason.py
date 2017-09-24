from api import SQLiteAPI

league = 'bl2'
seasons = ['2010', '2009', '2008', '2007', '2006']


api = SQLiteAPI.SQLiteAPI()
for season in seasons:
    api.import_season(league, season)
