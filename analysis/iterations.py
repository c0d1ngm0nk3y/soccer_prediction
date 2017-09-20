from prediction.NetTrainer import create_net, train_and_check
from prediction.Benchmark import verify
from analysis.Util import show_plot

def main():
    x_axis = []
    y_axis = []

    n = 30
    for i in range(0, n + 1, 2):
        net = create_net()
        x_axis.append(i)

        (result, _, _, _) = train_and_check(net, max_iterations=i)
        verified = verify(net)

        print 'Executed with ', i, 'iterations:', result, 'verified:', verified
        y_axis.append(result)

    show_plot(x_axis, y_axis, n)


if __name__ == "__main__":
    main()
