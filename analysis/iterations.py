import matplotlib.pyplot as plt
from NetTrainer import NetTrainer
from NeuralNetwork import NN2

x = []
y = []

n = 10
for i in range(0, n + 1):
    alpha = 0.9
    net = NN2(6, 4, 2, alpha)
    x.append(i)

    trainer = NetTrainer(net)
    trainer.train_season('bl1', '2016')
    result = 0
    for j in range(0, i):
        (_, _, _, _) = trainer.check_season('bl1', '2015')
        (_, _, _, _) = trainer.check_season('bl1', '2014')
        (result, _, _, _) = trainer.check_season('bl1', '2013')

    y.append(result)
print 'Result', max(y)

plt.plot(x, y, 'ro')
plt.axis([0, n, 0, 100])
plt.show()