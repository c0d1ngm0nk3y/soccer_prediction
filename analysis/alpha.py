import matplotlib.pyplot as plt

from NeuralNetwork import NN2
from prediction.NetTrainer import NetTrainer

x = []
y = []

n = 25
for i in range(0, n + 1):
    alpha = 0.1 * i
    net = NN2(6, 4, 2, alpha)
    x.append(alpha)

    trainer = NetTrainer(net)
    trainer.train_season('bl1', '2015')
    (result, _, _, _) = trainer.check_season('bl1', '2016')
    y.append(result)

plt.plot(x, y, 'ro')
plt.axis([0, n * 0.1, 0, 100])
plt.show()