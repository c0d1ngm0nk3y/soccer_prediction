from prediction.NetTrainer import NetTrainer, create_net, train_and_check
from prediction.Benchmark import verify
from prediction.Judger import create_judger
from analysis.Util import show_plot


def main():
    x_axis = []
    y_axis = []
    step = 0.01

    n = 20
    for i in range(0, n + 1):
        alpha = step * i
        net = create_net(alpha=alpha, output_layer=1)
        trainer = NetTrainer(net, create_judger("home"))
        x_axis.append(alpha)

        result = train_and_check(net, trainer=trainer)
        verified = verify(net, delta=1, trainer=trainer)
        print 'Executed with alpha', i * step, ':', result, 'verified', verified

        y_axis.append(result.get_performance())

    show_plot(x_axis, y_axis, n * step)


if __name__ == "__main__":
    main()
