#encoding=utf8
from prediction.Oracle import Oracle
from prediction.Benchmark import load_and_check

LEAGUE = 'bl1'
GAME_DAYS = [17, 18]

def get_net():
    filename = './prediction/pickles/20171001-03.pickles'
    net = load_and_check(filename)
    return net

def main():
    net = get_net()
    oracle = Oracle(net)

    for game_day in GAME_DAYS:
        print 'game day:', game_day
        games = oracle.predict_game_day(LEAGUE, '2017', game_day)
        for game in games:
            game.print_it(False)

if __name__ == '__main__':
    main()
