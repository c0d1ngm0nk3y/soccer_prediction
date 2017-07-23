import unittest
from NetTrainer import NetTrainer, PickHome, PickLeader
from NeuralNetwork import NN2


class MyTestCase(unittest.TestCase):

    def setUp(self):
        self.net = NN2(2,10,2,0.3)
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

    def test_training_improves(self):
        (result_1, _, _, _) = self.trainer.check_season('bl1', '2016')

        for i in range(0,10):
            self.trainer.train_season('bl1', '2015')

        (result_2, _, _, stats) = self.trainer.check_season('bl1', '2016')

        self.assertGreater(result_2, result_1)
        self.assertGreaterEqual(result_2, 55)
        self.assertGreaterEqual(stats[0], 10)
        self.assertGreaterEqual(stats[1], 96)
        self.assertGreaterEqual(stats[2], 27)

    def test_training_multiple(self):
        for i in range(0, 20):
            self.trainer.train_season('bl1', '2015')
            self.trainer.train_season('bl1', '2014')
            self.trainer.train_season('bl1', '2013')

        (result, _, _, stats) = self.trainer.check_season('bl1', '2016')

        self.assertGreaterEqual(result, 55)
        self.assertGreaterEqual(stats[0], 10)
        self.assertGreaterEqual(stats[1], 90)
        self.assertGreaterEqual(stats[2], 27)

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
