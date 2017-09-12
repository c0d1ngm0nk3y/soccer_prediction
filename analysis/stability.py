from prediction.NetTrainer import create_net, train_and_check
from analysis.Util import show_plot

x = []
y = []

n = 10
for i in range(0, n + 1):
    net = create_net()
    x.append(i + 1)

    (untrained, _, _, _) = train_and_check(net, [])
    (result, _, _, stats) = train_and_check(net,league='bl2')#, max_iterations=500, min_delta=0.1)
    print 'Executed ', i + 1, ':', untrained, '=>', result
    (result2, _, _, _) = train_and_check(net, [],league='bl1')
    print 'Executed 2', i + 1, ':', result2

    y.append(result)

show_plot(x, y, n)
