from api import SQLiteAPI

LEAGUE = 'bl2'
SEASONS = ['2017']


def main():
    api = SQLiteAPI.SQLiteAPI()
    for season in SEASONS:
        api.import_season(LEAGUE, season)

if __name__ == '__main__':
    main()
