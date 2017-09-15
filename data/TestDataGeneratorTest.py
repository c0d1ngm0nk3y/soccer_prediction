from __future__ import absolute_import
import unittest
from data.TestDataGenerator import TestDataGenerator

class GenerateData(unittest.TestCase):
    def setUp(self):
        self.gen = TestDataGenerator()

    def test_season(self):
        data = self.gen.generateFromSeason('bl1', '2014')

        self.assertTrue(len(data) > 100)
        self.assertTrue(len(data) < 1000)

        input_size = 16

        offenses = []
        defenses = []

        for d in data:
            (input, output, result, home_team) = d
            self.assertEqual(len(input), input_size)
            self.assertTrue(len(output) == 2)
            self.assertTrue(len(result) == 1)

            offenses.extend([input[6], input[(len(input) / 2) + 6]])
            defenses.extend([input[7], input[(len(input) / 2) + 7]])

            for i in range(0, input_size):
                self.assertTrue(input[i] > 0)
                self.assertTrue(input[i] <= 1)

            for i in range(0, 2):
                self.assertTrue(output[i] > 0)
                self.assertTrue(output[i] < 1)

            self.assertTrue(result[0] in [0,1,2])
        self.assertEqual(max(offenses), 1)
        self.assertLess(min(offenses), 0.1)

        self.assertEqual(max(defenses), 1)
        self.assertLess(min(defenses), 0.1)

    def test_get_output_0_0(self):
        output = self.gen.get_output_for_points(0,0)
        self.assertEqual(0.5, output)

    def test_get_output_5_5(self):
        output = self.gen.get_output_for_points(5, 5)
        self.assertEqual(0.5, output)

    def test_get_output_1_0(self):
        output = self.gen.get_output_for_points(1, 0)
        self.assertEqual(0.75, output)

    def test_get_output_2_1(self):
        output = self.gen.get_output_for_points(2, 1)
        self.assertEqual(0.75, output)

    def test_get_output_4_2(self):
        output = self.gen.get_output_for_points(4, 2)
        self.assertEqual(0.99, output)

    def test_get_output_3_0(self):
        output = self.gen.get_output_for_points(3, 0)
        self.assertEqual(0.99, output)

    def test_get_output_0_10(self):
        output = self.gen.get_output_for_points(0, 10)
        self.assertEqual(0.01, output)

    def test_get_output_4_0(self):
        output = self.gen.get_output_for_points(4, 0)
        self.assertEqual(0.99, output)

    def test_get_output_0_2(self):
        output = self.gen.get_output_for_points(0, 2)
        self.assertEqual(0.01, output)

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
