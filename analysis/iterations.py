from prediction.NetTrainer import create_net, train_and_check
from prediction.Benchmark import verify
from analysis.Util import show_plot

def main():
    x_axis = []
    y_axis = []

    n = 100
    alpha=0.05
    for i in range(0, n + 1, 5):
        net = create_net(alpha=alpha)
        x_axis.append(i)

        (result, _, _, stats) = train_and_check(net, max_iterations=i)
        verified = verify(net)

        print 'Executed with ', i, 'iterations:', result, 'verified:', verified, stats
        y_axis.append(result)

    show_plot(x_axis, y_axis, n)


if __name__ == "__main__":
    main()
