import unittest
from TestDataGenerator import TestDataGenerator


class GenerateData(unittest.TestCase):
    def test_season(self):
        gen = TestDataGenerator()
        data = gen.generateFromSeason('bl1', '2014')

        self.assertTrue(len(data) > 100)
        self.assertTrue(len(data) < 1000)

if __name__ == '__main__':
    unittest.main()
