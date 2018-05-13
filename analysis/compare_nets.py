import os
import logging
from analysis.Util import init_logging
from prediction.Benchmark import load_and_check


LEAGUE = 'bl2'
NET_PATH = "./prediction/pickles/" + LEAGUE

def main():
    logger = logging.getLogger()
    logger.setLevel(logging.DEBUG)
    for data_file in os.listdir(NET_PATH):
        if data_file.endswith(".pickles"):
            filename = os.path.join(NET_PATH, data_file)
            load_and_check(filename, league=LEAGUE)

if __name__ == '__main__':
    init_logging()
    main()
