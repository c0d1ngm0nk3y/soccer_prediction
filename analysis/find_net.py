from datetime import datetime
from time import time
from prediction.NetTrainer import create_net, train_and_check
from prediction.Benchmark import verify, load_and_check
from prediction.QueryStatistics import QueryStatistics
from prediction.Serializer import save_net

LEAGUE = 'bl1'

BEST_OF_N = 1000
FILENAME_TEMPLATE = './prediction/pickles/{}.pickles'
MIN_PERFORMANCE = 52
MIN_EXPECTATION = 1.00
VERIFY_THRESHOLD = 1
DEBUG = False

SEASONS = ['2006', '2007', '2008', '2009', '2010', '2011', '2012', '2013', '2014', '2015']

def find_net():
    best_net = None
    best_result = QueryStatistics()
    best_expectation = 0
    current_result_string = None
    for i in range(BEST_OF_N):
        if (i+1) % 10 == 0:
            print 'iteration', i+1, ':', current_result_string
        a_net = create_net()

        result = train_and_check(a_net, train_set=SEASONS, league=LEAGUE)
        if DEBUG:
            print result

        if (result.get_performance() < MIN_PERFORMANCE) \
                or (result.get_expected_win_ratio() < MIN_EXPECTATION):
            continue

        verified = verify(a_net, league=LEAGUE, delta=VERIFY_THRESHOLD, debug=DEBUG)
        if not verified:
            continue

        if result.get_performance() >= best_result.get_performance() \
                and result.get_expected_win_ratio() >= best_expectation:
            best_net = a_net
            best_result = result
            best_expectation = result.get_expected_win_ratio()
            current_result_string = "{}% / {}".format(best_result, best_expectation)

    print 'best net found:', best_result
    return best_net

def main():
    start_time = time()
    net = find_net()
    end_time = time()
    duration_min = int((end_time - start_time) / 60)
    if net:
        filename = FILENAME_TEMPLATE.format(datetime.now().strftime("%Y%m%d_%H%M"))
        print "Saving net: {}".format(filename)
        save_net(net, filename)
        load_and_check(filename)
    print "time for {} iterations: {} min".format(BEST_OF_N, duration_min)

if __name__ == '__main__':
    main()
