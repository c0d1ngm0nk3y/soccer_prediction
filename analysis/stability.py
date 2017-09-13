from prediction.NetTrainer import create_net, train_and_check
from analysis.Util import show_plot
from prediction.Benchmark import verify

x = []
y = []

n = 10
for i in range(0, n + 1):
    net = create_net()
    x.append(i + 1)

    (untrained, _, _, _) = train_and_check(net, [])
    (result, _, _, stats) = train_and_check(net,league='bl1')
    verified = verify(net)

    print 'Executed ', i + 1, ':', untrained, '=>', result, 'verified', verified

    y.append(result)

show_plot(x, y, n)
