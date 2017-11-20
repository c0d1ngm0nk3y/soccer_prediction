from api import SQLiteAPI

LEAGUE = 'bl1'
SEASON = '2017'
GAME_DAY = 12

def main():
    api = SQLiteAPI.SQLiteAPI()
    api.import_game_day(LEAGUE, SEASON, GAME_DAY, False)

if __name__ == '__main__':
    main()
