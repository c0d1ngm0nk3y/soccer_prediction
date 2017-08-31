import matplotlib.pyplot as plt

from prediction.NetTrainer import create_net, train_and_check

x = []
y = []
net = create_net()

i = 0
seasons = ['2011', '2012', '2013', '2014', '2015']
l = len(seasons)

for i in range(0, l):
    result = train_and_check(net, seasons[i:], '2016')
    x.append(i)
    y.append(result)

print 'Result', max(y)

plt.plot(x, y, 'ro')
plt.axis([0, i, 0, 100])
plt.show()