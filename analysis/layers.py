from prediction.NetTrainer import create_net, train_and_check
from analysis.Util import show_plot
from prediction.Benchmark import verify

x = []
y = []

START = 1
n = 10
for i in range(START, START + n + 1):
    net = create_net(hidden = i)
    x.append(i)

    (result, _, _, _) = train_and_check(net)
    verified = verify(net)

    print 'Executed with', i, 'hidden layers:', result, 'verified', verified
    y.append(result)

show_plot(x, y, START + n)
