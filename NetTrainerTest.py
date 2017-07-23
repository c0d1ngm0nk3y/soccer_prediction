import unittest
from NetTrainer import NetTrainer, PickHome, PickLeader
from NeuralNetwork import NN2


class MyTestCase(unittest.TestCase):

    def setUp(self):
        self.net = NN2(2,20,2,0.5)
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
        self.assertEqual(result, 24)

    def test_training_improves(self):
        (result_1, _, _, _) = self.trainer.check_season('bl1', '2016')

        for i in range(0,20):
            self.trainer.train_season('bl1', '2015')

        (result_2, _, _, stats) = self.trainer.check_season('bl1', '2016')

        self.assertGreater(result_2, result_1)
        self.assertEqual(result_2, 51)
        self.assertEqual(stats[0], 3)
        self.assertEqual(stats[1], 126)
        self.assertEqual(stats[2], 0)

    def _test_training_multiple(self):
        for i in range(0, 20):
            self.trainer.train_season('bl1', '2015')
            #self.trainer.train_season('bl1', '2014')
            #self.trainer.train_season('bl1', '2013')

        (result, _, _) = self.trainer.check_season('bl1', '2016')

        self.assertEqual(result, 99)


if __name__ == '__main__':
    unittest.main()
