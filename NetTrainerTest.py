import unittest
from NetTrainer import NetTrainer, PickHome, PickLeader
from NeuralNetwork import NN2

INPUT_SIZE = 6
ITERATIONS = 10

class MyTestCase(unittest.TestCase):

    def setUp(self):
        self.net = NN2(INPUT_SIZE, 10, 2, 0.3)
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
        self.assertEqual(result, 54)

    def isInRange(self, value, expected, range=3):
        self.assertLessEqual(value, expected + range)
        self.assertGreaterEqual(value, expected - range)

    def test_training_improves(self):
        (result_1, _, _, _) = self.trainer.check_season('bl1', '2016')

        for i in range(0, ITERATIONS):
            self.trainer.train_season('bl1', '2015')

        (result_2, _, _, stats) = self.trainer.check_season('bl1', '2016')

        self.assertGreater(result_2, result_1)
        self.isInRange(result_2, 67)
        self.isInRange(stats[0], 14)
        self.isInRange(stats[1], 104)
        self.isInRange(stats[2], 52)

    def test_training_multiple(self):
        for i in range(0, ITERATIONS):
            self.trainer.train_season('bl1', '2015')
            self.trainer.train_season('bl1', '2014')
            self.trainer.train_season('bl1', '2013')

        (result, _, _, stats) = self.trainer.check_season('bl1', '2016')

        self.isInRange(result, 67)
        self.isInRange(stats[0], 13)
        self.isInRange(stats[1], 103)
        self.isInRange(stats[2], 52)

    def test_check_2015(self):
        for i in range(0, ITERATIONS):
            self.trainer.train_season('bl1', '2016')
            self.trainer.train_season('bl1', '2014')
            self.trainer.train_season('bl1', '2013')

        (result, _, _, stats) = self.trainer.check_season('bl1', '2015')

        self.isInRange(result, 68)
        self.isInRange(stats[0], 16)
        self.isInRange(stats[1], 100)
        self.isInRange(stats[2], 60)

    def test_check_2014(self):
        for i in range(0, ITERATIONS):
            self.trainer.train_season('bl1', '2016')
            self.trainer.train_season('bl1', '2015')
            self.trainer.train_season('bl1', '2013')

        (result, _, _, stats) = self.trainer.check_season('bl1', '2014')

        self.isInRange(result, 68)
        self.isInRange(stats[0], 14)
        self.isInRange(stats[1], 105)
        self.isInRange(stats[2], 55)

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
