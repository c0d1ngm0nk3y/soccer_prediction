from prediction.Oracle import Oracle
from prediction.NetTrainer import train_and_check
from prediction.Serializer import load_net
from prediction.Benchmark import verify

LEAGUE = 'bl1'
GAME_DAYS = [10, 11, 12, 13]

def get_net():
    #filename = './prediction/pickles/20171001-03.pickles'
    filename = './prediction/pickles/20171120-02.pickles'
    net = load_net(filename)

    result = train_and_check(net, train_set=[])
    print 'choice:', result
    verify(net, debug=True)
    return net

def main():
    net = get_net()
    oracle = Oracle(net)

    for game_day in GAME_DAYS:
        print 'game day:', game_day
        games = oracle.predict_game_day(LEAGUE, '2017', game_day)
        for game in games:
            game.print_it(False)

if __name__ == '__main__':
    main()
