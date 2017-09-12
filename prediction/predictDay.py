from prediction.Oracle import Oracle
from prediction.NetTrainer import create_net, train_and_check
from prediction.Benchmark import verify

LEAGUE = 'bl1'
GAME_DAY = 3
BEST_OF_N = 5
TRIES = 3

def create_a_net():
    best_net = None
    best_result = 0
    for n in range(BEST_OF_N):
        net = create_net()
        (_, _, _, _) = train_and_check(net, ['2011','2012','2013','2014','2015','2016'], league='bl2')
        (result, _, _, _) = train_and_check(net, ['2011','2012','2013','2014','2015','2016'], league='bl1')
        if result > best_result:
            best_net = net
            best_result = result
    print 'best train:', best_result, '%'
    return best_net

for i in range(TRIES):
    net = create_a_net()
    if not verify(net):
        print 'verification failed'
    else:
        print 'verification successful'
        break

oracle = Oracle(net)
games = oracle.predict_game_day(LEAGUE, '2017', GAME_DAY)
for game in games:
    game.print_it(False)

