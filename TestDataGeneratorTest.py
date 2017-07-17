import unittest
from TestDataGenerator import TestDataGenerator
import numpy
import pandas
import matplotlib.pyplot as plt


class GenerateData(unittest.TestCase):
    def test_season(self):
        gen = TestDataGenerator()
        data = gen.generateFromSeason('bl1', '2014')

        self.assertTrue(len(data) > 100)
        self.assertTrue(len(data) < 1000)

        for d in data:
            (input, output, result) = d
            self.assertTrue(len(input) == 2)
            self.assertTrue(len(output) == 2)
            self.assertTrue(len(result) == 1)

            self.assertTrue(input[0] > 0)
            self.assertTrue(input[0] <= 1)

            self.assertTrue(output[0] > 0)
            self.assertTrue(output[0] < 1)

            self.assertTrue(result[0] in [0,1,2])

    def _test_season_explore(self):
        gen = TestDataGenerator()
        data = gen.generateFromSeason('bl1', '2014')

        print data

        l = len(data)
        x_train = numpy.zeros((l, 2), int)
        y = numpy.zeros((l,1), int)

        for i in range(0, l):
            (a , b) = data[i]
            y[i] = b[0]
            x_train[i][0] = a[0]
            x_train[i][1] = a[1]

        dataframe = pandas.DataFrame(x_train, columns=['home','away'])
        pandas.plotting.scatter_matrix(dataframe, c=y, figsize=(20, 20), s=1000)
        plt.show()

if __name__ == '__main__':
    unittest.main()
