from __future__ import absolute_import
import unittest
from prediction.NetTrainer import NetTrainer, PickHome, PickLeader
from NeuralNetwork import NN2

INPUT_SIZE = 6
ITERATIONS = 5

class MyTestCase(unittest.TestCase):

    def setUp(self):
        self.net = NN2(INPUT_SIZE, 6, 2, 0.9)
        self.trainer = NetTrainer(self.net)

    def test_initial_net(self):
        (result, hits, count, _) = self.trainer.check_season('bl1', '2016')

        self.assertGreater(hits, 0)
        self.assertEqual(count, 252)

        self.assertGreater(result, 1)
        self.assertLess(result, 100)

    def test_dummy_pick_home(self):
        self.net = PickHome()
        self.trainer = NetTrainer(self.net)

        (result, hits, count, _) = self.trainer.check_season('bl1', '2016')

        self.assertEqual(count, 252)
        self.assertEqual(result, 50)

    def test_dummy_pick_leader(self):
        self.net = PickLeader()
        self.trainer = NetTrainer(self.net)

        (result, hits, count, _) = self.trainer.check_season('bl1', '2016')

        self.assertEqual(count, 252)
        self.assertEqual(result, 47)

    #FIXME
    def isInRange(self, value, expected, range=5):
        self.assertLessEqual(value, expected + range)
        self.assertGreaterEqual(value, expected - range)

    def test_training_improves(self):
        (result_1, _, _, _) = self.trainer.check_season('bl1', '2016')

        for i in range(0, ITERATIONS):
            self.trainer.train_season('bl1', '2015')

        (result_2, _, _, stats) = self.trainer.check_season('bl1', '2016')

        self.assertGreater(result_2, result_1)
        self.isInRange(result_2, 42)
        self.isInRange(stats[0], 25)
        self.isInRange(stats[1], 76)
        #FIXME
        #self.isInRange(stats[2], 11)

    def test_check_2016(self):
        self.check_season_generic('2016', ['2015', '2014', '2013'], 40, 30, 72, 5)

    def test_check_2015(self):
        self.check_season_generic('2015', ['2016', '2014', '2013'], 43, 30, 71, 4)

    def test_check_2014(self):
        self.check_season_generic('2014', ['2016', '2015', '2013'], 41, 29, 69, 6)

    def check_season_generic(self, season, train_seasons, expected_result, expected_0, expected_1, expected_2):
        for i in range(0, ITERATIONS):
            for train_season in train_seasons:
                self.trainer.train_season('bl1', train_season)

        (result, _, _, stats) = self.trainer.check_season('bl1', season)

        self.isInRange(result, expected_result)
        self.isInRange(stats[0], expected_0)
        self.isInRange(stats[1], expected_1)

        #FIXME
        #self.isInRange(stats[2], expected_2)

    def test_interprete_0_low(self):
        result = self.trainer.interprete([0.4, 0.45])
        self.assertEqual(result, 0)

    def test_interprete_0_high(self):
        result = self.trainer.interprete([0.7, 0.6])
        self.assertEqual(result, 0)

    def test_interprete_0_middle(self):
        result = self.trainer.interprete([0.55, 0.45])
        self.assertEqual(result, 0)

    def test_interprete_0_middle_2(self):
        result = self.trainer.interprete([0.45, 0.55])
        self.assertEqual(result, 0)

    def test_interprete_1(self):
        result = self.trainer.interprete([0.6, 0.4])
        self.assertEqual(result, 1)

    def test_interprete_2(self):
        result = self.trainer.interprete([0.3, 0.7])
        self.assertEqual(result, 2)


if __name__ == '__main__':
    unittest.main()
