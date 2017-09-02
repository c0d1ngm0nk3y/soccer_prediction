from __future__ import absolute_import
import unittest
from prediction.NetTrainer import NetTrainer, PickHome, PickLeader, create_net, train_and_check

ITERATIONS = 5

class MyTestCase(unittest.TestCase):

    def setUp(self):
        self.net = create_net()
        self.trainer = NetTrainer(None)

    def test_not_trained_net(self):
        (result, hits, count, _) = train_and_check(self.net, [], '2016')

        self.assertGreater(hits, 0)
        self.assertEqual(count, 252)

        self.assertGreater(result, 1)
        self.assertLess(result, 100)

    def test_dummy_pick_home(self):
        self.net = PickHome()
        self.trainer = NetTrainer(self.net)

        (result, hits, count, _) = train_and_check(self.net, [], '2016')

        self.assertEqual(count, 252)
        self.assertEqual(result, 50)

    def test_dummy_pick_leader(self):
        self.net = PickLeader()
        self.trainer = NetTrainer(self.net)

        (result, hits, count, _) = train_and_check(self.net, [], '2016')

        self.assertEqual(count, 252)
        self.assertEqual(result, 47)

    #FIXME
    def isInRange(self, value, expected, range=4):
        self.assertLessEqual(value, expected + range)
        self.assertGreaterEqual(value, expected - range)

    def test_training_improves(self):
        (result_1, _, _, _) = train_and_check(self.net, [], '2016')

        (result_2, _, _, stats) = train_and_check(self.net, ['2015'], '2016')

        self.assertGreater(result_2, result_1)
        self.isInRange(result_2, 45, range=2)

        #FIXME
        #self.isInRange(stats[0], 30)
        #self.isInRange(stats[1], 74)
        #self.isInRange(stats[2], 11)

    def test_check_2016(self):
        self.check_season_generic('2016', ['2015'], 44, 29, 75, 15)

    def test_check_2015(self):
        self.check_season_generic('2015', ['2014'], 41, 29, 80, 7)

    def test_check_2014(self):
        self.check_season_generic('2014', ['2013'], 43, 26, 81, 15)

    def check_season_generic(self, season, train_seasons, expected_result, expected_0, expected_1, expected_2):

        (result, _, _, stats) = train_and_check(self.net, train_seasons, season)

        self.isInRange(result, expected_result, range=2)

        #FIXME
        #self.isInRange(stats[0], expected_0, range=8)
        #self.isInRange(stats[1], expected_1, range=8)
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
