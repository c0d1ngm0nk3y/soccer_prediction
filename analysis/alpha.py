from prediction.NetTrainer import create_net, train_and_check
from analysis.Util import show_plot
from prediction.Benchmark import verify

x = []
y = []
STEP = 0.025

n = 12
for i in range(0, n + 1):
    alpha = STEP * i
    net = create_net(alpha = alpha)
    x.append(alpha)

    (result, _, _, _) = train_and_check(net)
    verified = verify(net)
    print 'Executed with alpha', i * STEP, ':', result, 'verified', verified

    y.append(result)

show_plot(x, y, n * STEP)
