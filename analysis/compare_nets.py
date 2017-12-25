import os
from prediction.Benchmark import load_and_check

NET_PATH = "./prediction/pickles"

def main():
    for data_file in os.listdir(NET_PATH):
        if data_file.endswith(".pickles"):
            filename = os.path.join(NET_PATH, data_file)
            load_and_check(filename)

if __name__ == '__main__':
    main()
