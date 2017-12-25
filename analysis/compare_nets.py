import os
from prediction.NetTrainer import train_and_check
from prediction.Serializer import load_net
from prediction.Benchmark import verify

NET_PATH = "./prediction/pickles"

def check_net(filename):
    net = load_net(filename)

    result = train_and_check(net, train_set=[])
    print filename, result
    verify(net, debug=True)
    return net


def main():
    for data_file in os.listdir(NET_PATH):
        if data_file.endswith(".pickles"):
            filename = os.path.join(NET_PATH, data_file)
            check_net(filename)

if __name__ == '__main__':
    main()
