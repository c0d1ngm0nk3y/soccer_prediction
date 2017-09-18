from prediction.NetTrainer import create_net, train_and_check
from analysis.Util import show_plot
from prediction.Benchmark import verify

x = []
y = []

n = 30
for i in range(0, n + 1, 2):
    net = create_net()
    x.append(i)

    (result, _, _, _) = train_and_check(net, max_iterations= i)
    verified = verify(net)

    print 'Executed with ', i, 'iterations:', result, 'verified:', verified
    y.append(result)

show_plot(x, y, n)
