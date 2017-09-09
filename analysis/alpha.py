from prediction.NetTrainer import create_net, train_and_check
from analysis.Util import show_plot

x = []
y = []
STEP = 0.025

n = 16
for i in range(0, n + 1):
    alpha = STEP * i
    net = create_net(alpha = alpha)
    x.append(alpha)

    (result, _, _, _) = train_and_check(net)
    print 'Executed with alpha', i * STEP, ':', result

    y.append(result)

show_plot(x, y, n * STEP)
