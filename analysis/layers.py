from prediction.NetTrainer import create_net, train_and_check
from analysis.Util import show_plot

x = []
y = []

n = 20
for i in range(1, n + 1):
    net = create_net(hidden = i)
    x.append(i)

    (result, _, _, _) = train_and_check(net)
    print 'Executed with', i, 'hidden layers:', result
    y.append(result)

show_plot(x, y, n)
