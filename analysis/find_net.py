from prediction.Oracle import Oracle
from prediction.NetTrainer import create_net, train_and_check
from prediction.Benchmark import verify
from prediction.QueryStatistics import QueryStatistics
from prediction.Serializer import save_net

LEAGUE = 'bl1'

BEST_OF_N = 200
FILENAME = './prediction/pickles/20171113-01.pickles'
MIN_PERFORMANCE = 49
MIN_EXPECTATION = 1.06
VERIFY_THRESHOLD = 1

SEASONS = ['2006', '2007', '2008', '2009', '2010', '2011', '2012', '2013', '2014', '2015']

def find_net():
    best_net = None
    best_result = QueryStatistics()
    best_expectation = 0
    for i in range(BEST_OF_N):
        if (i+1) % 10 == 0:
           print 'iteration', i+1
        a_net = create_net()

        result = train_and_check(a_net, train_set=SEASONS, league=LEAGUE)
        print result

        if (result.get_performance() < MIN_PERFORMANCE) or (result.get_expected_win_ratio() < MIN_EXPECTATION):
            continue

        verified = verify(a_net, league=LEAGUE, delta=VERIFY_THRESHOLD, debug=False)
        if not verified:
            continue

        if result.get_performance() >= best_result.get_performance() \
                and result.get_expected_win_ratio() >= best_expectation:
            best_net = a_net
            best_result = result
            best_expectation = result.get_expected_win_ratio()

    print 'choice:', best_result
    return best_net

net = find_net()
if not net:
    print 'no net found!!!'
else:
    verify(net, league=LEAGUE, delta=VERIFY_THRESHOLD, debug=True)
    save_net(net, FILENAME)


