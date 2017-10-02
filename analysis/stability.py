from prediction.NetTrainer import create_net, train_and_check
from prediction.Benchmark import verify
from analysis.Util import show_plot


def main():
    x_axis = []
    y_axis = []

    n = 15
    for i in range(0, n + 1):
        net = create_net()
        x_axis.append(i + 1)

        untrained = train_and_check(net, [])
        trained = train_and_check(net)
        verified = verify(net, debug=False, delta=2)

        print 'Execution {0}:'.format(i+1), untrained.get_performance(),\
            '=>', trained, 'verified:', verified

        y_axis.append(trained.get_performance())

    show_plot(x_axis, y_axis, n)

if __name__ == "__main__":
    main()
