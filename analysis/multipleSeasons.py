from prediction.NetTrainer import create_net, train_and_check
from analysis.Util import show_plot

x = []
y = []
net = create_net()

i = 0
seasons = ['2011', '2012', '2013', '2014', '2015']
l = len(seasons)

for i in range(0, l+1):
    (result, _, _, _) = train_and_check(net, seasons[i:], '2016')
    print 'Executed with', l-i, 'seasons:', result

    x.append(l-i)
    y.append(result)

show_plot(x, y, i)