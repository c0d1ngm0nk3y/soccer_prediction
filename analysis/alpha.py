from prediction.NetTrainer import create_net, train_and_check
from prediction.Benchmark import verify
from analysis.Util import show_plot


def main():
    x_axis = []
    y_axis = []
    step = 0.025

    n = 12
    for i in range(0, n + 1):
        alpha = step * i
        net = create_net(alpha=alpha)
        x_axis.append(alpha)

        (result, _, _, _) = train_and_check(net)
        verified = verify(net)
        print 'Executed with alpha', i * step, ':', result, 'verified', verified

        y_axis.append(result)

    show_plot(x_axis, y_axis, n * step)


if __name__ == "__main__":
    main()
