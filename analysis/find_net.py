import logging
from datetime import datetime
from time import time
from analysis.Util import init_logging
from prediction.NetTrainer import create_net, train_and_check
from prediction.Benchmark import verify, load_and_check, calculate_points
from prediction.QueryStatistics import QueryStatistics
from prediction.Serializer import save_net

LEAGUE = 'bl1'

BEST_OF_N = 2
FILENAME_TEMPLATE = './prediction/pickles/' + LEAGUE + '/{}.pickles'
DEBUG = False

SEASONS = ['2006', '2007', '2008', '2009', '2010', '2011', '2012', '2013', '2014', '2015', '2016']

def find_net():
    logger = logging.getLogger()
    best_net = None
    best_result = QueryStatistics()
    best_points = 0
    current_result_string = None

    for i in range(BEST_OF_N):
        if (i+1) % 10 == 0:
            logger.info('iteration %d: %s', i+1, current_result_string)
        a_net = create_net()

        query_stats = train_and_check(a_net, train_set=SEASONS, league=LEAGUE, check='2017')
        (_, verify_result) = verify(a_net, league=LEAGUE)

        points = calculate_points(query_stats, verify_result)

        if points <= best_points:
            continue

        best_net = a_net
        best_result = query_stats
        best_points = points
        current_result_string = "{}%  ({})".format(best_result, best_points)

    logger.warning('best net found: %s', best_result)
    return best_net

def main():
    logger = logging.getLogger()
    start_time = time()
    logger.warning('searching net with %d iterations', BEST_OF_N)
    net = find_net()
    end_time = time()
    duration_min = int((end_time - start_time) / 60)
    if net:
        filename = FILENAME_TEMPLATE.format(datetime.now().strftime("%Y%m%d_%H%M"))
        logger.info("saving net: %s", filename)
        save_net(net, filename)
        load_and_check(filename, league=LEAGUE)
    logger.warning("time for %d iterations: %d min", BEST_OF_N, duration_min)

if __name__ == '__main__':
    init_logging()
    main()
