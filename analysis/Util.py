#encoding=utf8
import logging
import matplotlib.pyplot as plt

def show_plot(coord_x, coord_y, max_x):
    print 'result', min(coord_y), '<->', max(coord_y)

    plt.plot(coord_x, coord_y, 'ro')
    plt.axis([0, max_x, 0, 100])
    plt.show()

def init_logging():
    log_format = '%(asctime)-15s %(levelno)s %(message)s'
    logging.basicConfig(format=log_format)
    logging.getLogger().setLevel(logging.INFO)

def string_with_fixed_length(string):
    return string.replace('ü', 'u').replace('ö', 'o').replace('ä', 'a')
