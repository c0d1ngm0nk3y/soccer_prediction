import os
from prediction.Benchmark import load_and_check

NET_PATH_PREFIX = "./prediction/pickles/"

class CompareAction(object):
    def compare_nets(self, league):
        nets = []
        for data_file in os.listdir(NET_PATH_PREFIX + league):
            if data_file.endswith(".pickles"):
                filename = os.path.join(NET_PATH_PREFIX, league,  data_file)
                (_, entry) = load_and_check(filename, league=league)
                nets.append(entry)

        return nets
