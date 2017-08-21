import SQLiteAPI

league = 'bl2'
season = '2017'
game_day = 3


api = SQLiteAPI.SQLiteAPI()
api.import_game_day(league, season, game_day, False)
