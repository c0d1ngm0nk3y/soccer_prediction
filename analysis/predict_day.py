from prediction.Oracle import Oracle
from prediction.NetTrainer import create_net, train_and_check
from prediction.Benchmark import verify

LEAGUE = 'bl1'
GAME_DAY = 5

BEST_OF_N = 5
TRIES = 30

SEASONS = ['2009', '2010', '2011', '2012', '2013', '2014', '2015']
#SEASONS = ['2013', '2014', '2015']

def create_a_net():
    best_net = None
    best_result = 0
    for _ in range(BEST_OF_N):
        a_net = create_net()
        (result, _, _, _) = train_and_check(a_net, train_set=SEASONS, league='bl1', train_leagues=['bl1'])
        if result > best_result and verify(a_net, delta=1, debug=True):
            best_net = a_net
            best_result = result
    if best_net:
        (result2, _, _, _) = train_and_check(best_net, train_set=[], league='bl2')
    else:
        result2 = 0

    print 'best train:', best_result, '% (', result2, '%)'
    return best_net

for i in range(TRIES):
    net = create_a_net()
    if net:
        break
    print 'no net found...'

if not net:
    raise BaseException('no net created')

ORACLE = Oracle(net)
GAMES = ORACLE.predict_game_day(LEAGUE, '2017', GAME_DAY)
for game in GAMES:
    game.print_it(False)
