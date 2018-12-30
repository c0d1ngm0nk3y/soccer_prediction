from prediction.NetTrainer import NetTrainer, create_net, train_and_check
from prediction.Judger import create_judger
from prediction.Benchmark import verify
from analysis.Util import show_plot


def main():
    x_axis = []
    y_axis = []

    start = 5
    n = 10
    for i in range(start, start + n + 1):

        net = create_net(hidden_layer=i, output_layer=1)
        trainer = NetTrainer(net, create_judger("home"))

        x_axis.append(i)

        result = train_and_check(net, trainer=trainer)
        verified = verify(net, trainer=trainer)

        print 'Executed with', i, 'hidden layers:', result, 'verified', verified
        y_axis.append(result.get_performance())

    show_plot(x_axis, y_axis, start + n)


if __name__ == "__main__":
    main()
