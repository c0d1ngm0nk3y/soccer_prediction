from api import SQLiteAPI

league = 'bl1'
season = '2017'
#game_day = 6

api = SQLiteAPI.SQLiteAPI()
for game_day in range(4, 35):
    api.import_game_day(league, season, game_day, False)
