import os
from prediction.Benchmark import load_and_check

NET_PATH_PREFIX = "./prediction/pickles/"

class CompareAction(object):
    def compare_nets(self, league, _type):
        nets = []
        for data_file in os.listdir(NET_PATH_PREFIX + league + "/" + _type):
            if data_file.endswith(".pickles"):
                filename = os.path.join(NET_PATH_PREFIX, league, _type, data_file)
                (_, entry) = load_and_check(filename, league=league, _type=_type)
                nets.append(entry)

        return sorted(nets, key=lambda x: x.points, reverse=True)
