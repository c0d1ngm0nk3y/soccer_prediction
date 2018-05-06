#encoding=utf8
import logging
from analysis.Util import init_logging
from prediction.Oracle import Oracle
from prediction.Benchmark import load_and_check

LEAGUE = 'bl1'
GAME_DAYS = [33, 34]

def get_net():
    filename = './prediction/pickles/20180404_2210.pickles'
    net = load_and_check(filename)
    return net

def main():
    logger = logging.getLogger()
    net = get_net()
    oracle = Oracle(net)

    for game_day in GAME_DAYS:
        logger.info('game day: %d', game_day)
        games = oracle.predict_game_day(LEAGUE, '2017', game_day)
        print('*' * 100)
        for game in games:
            game.print_it()
        print('*' * 100)

if __name__ == '__main__':
    init_logging()
    main()
