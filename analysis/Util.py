import matplotlib.pyplot as plt

def show_plot(coord_x, coord_y, max_x):
    print 'result', min(coord_y), '<->', max(coord_y)

    plt.plot(coord_x, coord_y, 'ro')
    plt.axis([0, max_x, 0, 100])
    plt.show()
