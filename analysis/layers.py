import matplotlib.pyplot as plt

from prediction.NetTrainer import create_net, train_and_check

x = []
y = []

n = 30
for i in range(0, n + 1):
    alpha = 1.1
    net = create_net(hidden = i)
    x.append(i)

    result = train_and_check(net, ['2015'], '2016')
    y.append(result)
print 'Result', max(y)

plt.plot(x, y, 'ro')
plt.axis([0, n, 0, 100])
plt.show()