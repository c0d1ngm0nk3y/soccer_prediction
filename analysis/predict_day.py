#encoding=utf8
import logging
from analysis.Util import init_logging
from prediction.Oracle import Oracle
from prediction.Benchmark import load_and_check
from prediction.Judger import create_judger
from prediction.NetProxy import NetProxy
from actions.CompareAction import CompareAction

LEAGUE = 'bl1'
GAME_DAYS = range(1, 31)
SEASON = '2018'

TYPE = "default"

def get_combined_net():
    home_net = get_net("home")
    away_net = get_net("away")
    net = NetProxy(home_net, away_net)
    return net

def get_net(_type):
    if _type == "combined":
        net = get_combined_net()
        return net
    action = CompareAction()
    nets = action.compare_nets(league=LEAGUE, _type=_type)
    filename = nets[0].path
    logger = logging.getLogger()
    logger.info('loading: %s', filename)
    (net, _) = load_and_check(filename, league=LEAGUE, _type=_type)
    return net

def main():
    logger = logging.getLogger()
    net = get_net(TYPE)

    judger = create_judger(TYPE)
    oracle = Oracle(net=net, judger=judger)

    correct = 0

    for game_day in GAME_DAYS:
        logger.info('game day: %d', game_day)
        games = oracle.predict_game_day(LEAGUE, SEASON, game_day)
        print('*' * 100)
        for game in games:
            #if game.get_actual_result() != 0:
             #   continue

            #print game.v_out
            game.print_it()
            if game.is_correct():
                correct = correct + 1
        print('*' * 100)
    print('Correct: {} of {}'.format(correct, 9*len(GAME_DAYS)))

if __name__ == '__main__':
    init_logging()
    main()
