from prediction.NetTrainer import create_net, train_and_check
from analysis.Util import show_plot

x = []
y = []

n = 15
for i in range(0, n + 1):
    net = create_net(alpha = 0.05)
    x.append(i + 1)

    (untrained, _, _, _) = train_and_check(net, [])
    (result, _, _, _) = train_and_check(net, ['2015'], iterations=100)
    print 'Executed ', i + 1, ':', untrained, '=>', result

    y.append(result)

show_plot(x, y, n)
