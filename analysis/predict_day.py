from prediction.Oracle import Oracle
from prediction.NetTrainer import train_and_check
from prediction.Serializer import load_net
from prediction.Benchmark import verify

LEAGUE = 'bl1'
GAME_DAYS = [9, 10, 11, 12]

def get_net():
    filename = './prediction/pickles/20171001-03.pickles'
    net = load_net(filename)

    result = train_and_check(net, train_set=[])
    print 'choice:', result
    verify(net, debug=True)
    return net

net = get_net()
ORACLE = Oracle(net)

for game_day in GAME_DAYS:
    print 'game day:', game_day
    GAMES = ORACLE.predict_game_day(LEAGUE, '2017', game_day)
    for game in GAMES:
        game.print_it(False)
