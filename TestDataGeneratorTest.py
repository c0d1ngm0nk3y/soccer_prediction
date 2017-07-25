import unittest
from TestDataGenerator import TestDataGenerator
import numpy
import pandas
#import matplotlib.pyplot as plt


class GenerateData(unittest.TestCase):
    def setUp(self):
        self.gen = TestDataGenerator()

    def test_season(self):
        data = self.gen.generateFromSeason('bl1', '2014')

        self.assertTrue(len(data) > 100)
        self.assertTrue(len(data) < 1000)

        for d in data:
            (input, output, result) = d
            self.assertTrue(len(input) == 4)
            self.assertTrue(len(output) == 2)
            self.assertTrue(len(result) == 1)

            for i in range(0, 4):
                self.assertTrue(input[i] > 0)
                self.assertTrue(input[i] <= 1)

            for i in range(0, 2):
                self.assertTrue(output[i] > 0)
                self.assertTrue(output[i] < 1)

            self.assertTrue(result[0] in [0,1,2])

    def _test_season_explore(self):
        data = self.gen.generateFromSeason('bl1', '2014')

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

    def test_get_output_0_0(self):
        output = self.gen.get_output_for_points(0,0)
        self.assertEqual(0.5, output)

    def test_get_output_5_5(self):
        output = self.gen.get_output_for_points(5, 5)
        self.assertEqual(0.5, output)

    def test_get_output_1_0(self):
        output = self.gen.get_output_for_points(1, 0)
        self.assertEqual(0.65, output)

    def test_get_output_2_1(self):
        output = self.gen.get_output_for_points(2, 1)
        self.assertEqual(0.65, output)

    def test_get_output_4_2(self):
        output = self.gen.get_output_for_points(4, 2)
        self.assertEqual(0.8, output)

    def test_get_output_3_0(self):
        output = self.gen.get_output_for_points(3, 0)
        self.assertEqual(0.95, output)

    def test_get_output_0_10(self):
        output = self.gen.get_output_for_points(0, 10)
        self.assertEqual(0.01, output)

    def test_get_output_4_0(self):
        output = self.gen.get_output_for_points(4, 0)
        self.assertEqual(0.99, output)

    def test_get_output_0_2(self):
        output = self.gen.get_output_for_points(0, 2)
        self.assertEqual(0.2, output)

    def test_get_input_1(self):
        input = self.gen.get_input_for_position(1)
        self.assertEqual(1, input)

    def test_get_input_18(self):
        input = self.gen.get_input_for_position(18)
        self.assertEqual(0.01, input)

    def test_get_input_9(self):
        input = self.gen.get_input_for_position(9)
        self.assertEqual(0.53, input)


if __name__ == '__main__':
    unittest.main()
