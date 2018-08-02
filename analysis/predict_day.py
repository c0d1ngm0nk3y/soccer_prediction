#encoding=utf8
import logging
from analysis.Util import init_logging
from prediction.Oracle import Oracle
from prediction.Benchmark import load_and_check

LEAGUE = 'bl1'
GAME_DAYS = [1]
SEASON = '2018'
NETS = {'bl1': './prediction/pickles/bl1/20180404_2210.pickles',
        'bl2': './prediction/pickles/bl2/20180513_1728.pickles'}

def get_net():
    filename = NETS[LEAGUE]
    (net, _) = load_and_check(filename, league=LEAGUE)
    return net

def main():
    logger = logging.getLogger()
    net = get_net()
    oracle = Oracle(net)

    for game_day in GAME_DAYS:
        logger.info('game day: %d', game_day)
        games = oracle.predict_game_day(LEAGUE, '2018', game_day)
        print('*' * 100)
        for game in games:
            game.print_it()
        print('*' * 100)

if __name__ == '__main__':
    init_logging()
    main()
