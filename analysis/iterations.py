import matplotlib.pyplot as plt

from prediction.NetTrainer import create_net, train_and_check

x = []
y = []

n = 20
for i in range(0, n + 1):
    net = create_net()
    x.append(i)

    result = train_and_check(net, ['2015'], '2016', iterations = i)
    y.append(result)
print 'Result', max(y)

plt.plot(x, y, 'ro')
plt.axis([0, n, 0, 100])
plt.show()