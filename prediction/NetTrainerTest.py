from __future__ import absolute_import
import unittest
from prediction.NetTrainer import NetTrainer, PickHome, PickLeader, create_net, train_and_check
from prediction.judger.DrawDiff import interprete

ITERATIONS = 5

class MyTestCase(unittest.TestCase):

    def setUp(self):
        self.net = create_net()
        self.trainer = NetTrainer(None)

    def test_not_trained_net(self):
        result = train_and_check(self.net, [], '2016')

        self.assertGreater(result.get_hits(), 0)
        self.assertEqual(result.get_count(), 252)

        self.assertGreater(result.get_performance(), 1)
        self.assertLess(result.get_performance(), 100)

    def test_dummy_pick_home(self):
        self.net = PickHome()
        self.trainer = NetTrainer(self.net)

        result = train_and_check(self.net, [], '2016')

        self.assertEqual(result.get_count(), 252)
        self.assertEqual(result.get_performance(), 50)

    def test_dummy_pick_leader(self):
        self.net = PickLeader()
        self.trainer = NetTrainer(self.net)

        result = train_and_check(self.net, [], '2016')

        self.assertEqual(result.get_count(), 252)
        self.assertEqual(result.get_performance(), 47)

    def is_in_range(self, value, expected, range_value):
        self.assertLessEqual(value, expected + range_value)
        self.assertGreaterEqual(value, expected - range_value)

    def test_training_improves(self):
        for _ in range(0, 3):
            result_1 = train_and_check(self.net, [], '2016')
            if result_1.get_performance() >= 50:
                self.net = create_net()
            else:
                break

        result_2 = train_and_check(self.net, ['2015'], '2016')

        self.assertGreater(result_2.get_performance(), result_1.get_performance())
        self.is_in_range(result_2.get_performance(), 45, range_value=5)

        stats = result_2.get_statistics()
        self.assertGreater(stats[0], 5)
        self.assertGreater(stats[1], 5)
        self.assertGreater(stats[2], 3)

    def test_check_2016(self):
        self.check_season_generic('2016', ['2015'], 47)

    def test_check_2015(self):
        self.check_season_generic('2015', ['2014', '2013'], 44)

    def test_check_2014(self):
        self.check_season_generic('2014', ['2013'], 46)

    def check_season_generic(self, season, train_seasons, expected_result):

        result = train_and_check(self.net, train_seasons, season)

        #print stats
        self.is_in_range(result.get_performance(), expected_result, range_value=5)

        stats = result.get_statistics()
        self.assertGreater(stats[0], 5)
        self.assertGreater(stats[1], 5)
        self.assertGreater(stats[2], 3)

    def test_interprete_0_low(self):
        result = interprete([0.4, 0.45])
        self.assertEqual(result, 0)

    def test_interprete_0_high(self):
        result = interprete([0.7, 0.6])
        self.assertEqual(result, 0)

    def test_interprete_0_middle(self):
        result = interprete([0.58, 0.48])
        self.assertEqual(result, 0)

    def test_interprete_0_middle_2(self):
        result = interprete([0.48, 0.58])
        self.assertEqual(result, 0)

    def test_interprete_1(self):
        result = interprete([0.61, 0.39])
        self.assertEqual(result, 1)

    def test_interprete_2(self):
        result = interprete([0.3, 0.7])
        self.assertEqual(result, 2)


if __name__ == '__main__':
    unittest.main()
