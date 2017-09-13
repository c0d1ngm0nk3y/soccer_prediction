from prediction.NetTrainer import create_net, train_and_check
from analysis.Util import show_plot
from prediction.Benchmark import verify

x = []
y = []
i = 0
seasons = ['2011', '2012', '2013', '2014', '2015']
l = len(seasons)

for i in range(0, l+1):
    net = create_net()
    (result, _, _, _) = train_and_check(net, seasons[i:], '2016')
    verified = verify(net)
    print 'Executed with', l-i, 'seasons:', result, 'verified', verified

    x.append(l-i)
    y.append(result)

show_plot(x, y, i)