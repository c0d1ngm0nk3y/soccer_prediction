from api import SQLiteAPI

league = 'bl1'
season = '2017'
game_day = 11

api = SQLiteAPI.SQLiteAPI()
api.import_game_day(league, season, game_day, False)
