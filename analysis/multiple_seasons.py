from prediction.NetTrainer import create_net, train_and_check
from prediction.Benchmark import verify
from analysis.Util import show_plot

def main():
    x_axis = []
    y_axis = []
    i = 0
    seasons = ['2011', '2012', '2013', '2014', '2015']
    length = len(seasons)

    for i in range(0, length+1):
        net = create_net()
        (result, _, _, _) = train_and_check(net, seasons[i:], '2016')
        verified = verify(net)
        print 'Executed with', length-i, 'seasons:', result, 'verified', verified

        x_axis.append(length-i)
        y_axis.append(result)

    show_plot(x_axis, y_axis, i)


if __name__ == "__main__":
    main()
