from prediction.Oracle import Oracle
from prediction.NetTrainer import create_net, train_and_check

LEAGUE = 'bl1'
GAME_DAY = 30

def create_a_net():
    net = create_net()
    (result, _, _, _) = train_and_check(net, ['2011','2012','2013','2014','2015'], '2016', league=LEAGUE)
    print 'train:', result, '%'
    return net

net = create_a_net()
oracle = Oracle(net)

games = oracle.predict_game_day(LEAGUE, '2016', GAME_DAY)
for game in games:
    game.print_it()

