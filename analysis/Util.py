import matplotlib.pyplot as plt

def show_plot(x, y, max_x):
    print 'Result', max(y)

    plt.plot(x, y, 'ro')
    plt.axis([0, max_x, 0, 100])
    plt.show()