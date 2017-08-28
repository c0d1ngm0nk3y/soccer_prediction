from prediction.Oracle import Oracle
from NeuralNetwork import NN2
from prediction.NetTrainer import NetTrainer

ITERATIONS = 5

def create_net():
    alpha = 0.9
    net = NN2(6, 4, 2, alpha)

    trainer = NetTrainer(net)
    trainer.train_season('bl1', '2013')
    trainer.train_season('bl1', '2014')
    trainer.train_season('bl1', '2015')

    return net

net = create_net()
oracle = Oracle(net)
games = oracle.predict_game_day('bl1', '2016', 34)

for game in games:
    game.print_it()