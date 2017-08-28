import matplotlib.pyplot as plt

from NeuralNetwork import NN2
from prediction.NetTrainer import NetTrainer

x = []
y = []

n = 10
for i in range(0, n + 1):
    alpha = 0.9
    net = NN2(6, 4, 2, alpha)
    x.append(i)

    trainer = NetTrainer(net)
    result = 0
    for j in range(0, i):
        trainer.train_season('bl1', '2013')
        trainer.train_season('bl1', '2014')
        trainer.train_season('bl1', '2015')

    (result, _, _, _) = trainer.check_season('bl1', '2016')

    y.append(result)
print 'Result', max(y)

plt.plot(x, y, 'ro')
plt.axis([0, n, 0, 100])
plt.show()