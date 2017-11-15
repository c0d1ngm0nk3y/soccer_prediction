from api import SQLiteAPI

LEAGUE = 'bl2'
SEASONS = ['2010', '2009', '2008', '2007', '2006']


def main():
    api = SQLiteAPI.SQLiteAPI()
    for season in SEASONS:
        api.import_season(LEAGUE, season)

if __name__ == '__main__':
    main()
