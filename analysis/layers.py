from prediction.NetTrainer import create_net, train_and_check
from prediction.Benchmark import verify
from analysis.Util import show_plot


def main():
    x_axis = []
    y_axis = []

    start = 1
    n = 10
    for i in range(start, start + n + 1):
        net = create_net(hidden_layer=i)
        x_axis.append(i)

        (result, _, _, _) = train_and_check(net)
        verified = verify(net)

        print 'Executed with', i, 'hidden layers:', result, 'verified', verified
        y_axis.append(result)

    show_plot(x_axis, y_axis, start + n)


if __name__ == "__main__":
    main()
