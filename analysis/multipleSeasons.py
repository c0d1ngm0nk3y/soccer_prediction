import matplotlib.pyplot as plt

from NeuralNetwork import NN2
from prediction.NetTrainer import NetTrainer

x = []
y = []
alpha = 0.1
net = NN2(6, 10, 2, alpha)
trainer = NetTrainer(net)

i = 0
for r in range(0,10):
    for season in ['2011', '2012', '2013', '2014', '2015']:
        trainer.train_season('bl1', season)
        (result, _, _, _) = trainer.check_season('bl1', '2016')
        i = i + 1
        x.append(i)
        y.append(result)

        trainer.train_season('bl2', season)
        (result, _, _, _) = trainer.check_season('bl1', '2016')
        i = i + 1
        x.append(i)
        y.append(result)

print 'Result', max(y)

plt.plot(x, y, 'ro')
plt.axis([0, i, 50, 100])
plt.show()