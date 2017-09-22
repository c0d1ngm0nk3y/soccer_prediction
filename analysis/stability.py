from prediction.NetTrainer import create_net, train_and_check
from prediction.Benchmark import verify
from analysis.Util import show_plot

def main():
    x_axis = []
    y_axis = []

    n = 20
    for i in range(0, n + 1):
        net = create_net()
        x_axis.append(i + 1)

        (untrained, _, _, _) = train_and_check(net, [])
        (result, _, _, _) = train_and_check(net, league='bl1')
        verified = verify(net, debug=False)

        print 'Executed ', i + 1, ':', untrained, '=>', result, 'verified', verified

        y_axis.append(result)

    show_plot(x_axis, y_axis, n)

if __name__ == "__main__":
    main()
