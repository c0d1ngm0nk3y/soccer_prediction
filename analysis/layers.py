import matplotlib.pyplot as plt

from NeuralNetwork import NN2
from prediction.NetTrainer import NetTrainer

x = []
y = []

n = 30
for i in range(1, n + 1):
    alpha = 1.1
    net = NN2(6, i, 2, alpha)
    x.append(i)

    trainer = NetTrainer(net)
    trainer.train_season('bl1', '2015')
    (_, _, _, _) = trainer.check_season('bl1', '2016')
    (_, _, _, _) = trainer.check_season('bl1', '2014')
    (result, _, _, _) = trainer.check_season('bl1', '2013')

    y.append(result)
print 'Result', max(y)

plt.plot(x, y, 'ro')
plt.axis([0, n, 35, 50])
plt.show()