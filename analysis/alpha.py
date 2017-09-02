import matplotlib.pyplot as plt

from prediction.NetTrainer import create_net, train_and_check

x = []
y = []

n = 25
for i in range(0, n + 1):
    alpha = 0.1 * i
    net = create_net(alpha = alpha)
    x.append(alpha)

    (result, _, _, _) = train_and_check(net, ['2015'], '2016')
    y.append(result)

print 'Result', max(y)

plt.plot(x, y, 'ro')
plt.axis([0, n * 0.1, 0, 100])
plt.show()