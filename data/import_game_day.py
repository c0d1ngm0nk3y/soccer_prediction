from api import SQLiteAPI

LEAGUE = 'bl1'
SEASON = '2018'
GAME_DAY = 8


def main():
    api = SQLiteAPI.SQLiteAPI()
    api.import_game_day(LEAGUE, SEASON, GAME_DAY, False)

if __name__ == '__main__':
    main()
