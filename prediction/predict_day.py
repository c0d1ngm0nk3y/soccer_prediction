from prediction.Oracle import Oracle
from prediction.NetTrainer import create_net, train_and_check
from prediction.Benchmark import verify

LEAGUE = 'bl2'
GAME_DAY = 5
BEST_OF_N = 1
TRIES = 1

SEASONS = ['2011', '2012', '2013', '2014', '2015', '2016']

def create_a_net():
    best_net = None
    best_result = 0
    for _ in range(BEST_OF_N):
        a_net = create_net()
        (result, _, _, _) = train_and_check(a_net, SEASONS, league='bl1')
        if result > best_result and verify(a_net):
            best_net = a_net
            best_result = result
    print 'best train:', best_result, '%'
    return best_net

for i in range(TRIES):
    net = create_a_net()
    if not net:
        raise BaseException('no net created')

ORACLE = Oracle(net)
GAMES = ORACLE.predict_game_day(LEAGUE, '2017', GAME_DAY)
for game in GAMES:
    game.print_it(False)
