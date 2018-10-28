from __future__ import absolute_import
import unittest
from prediction.Benchmark import verify, calculate_points
from prediction.NetTrainer import PickAway, create_net, train_and_check
from prediction.QueryStatistics import QueryStatistics

class BenchmarkTest(unittest.TestCase):
    def test_pick_leader_wont_verify(self):
        net = PickAway()
        (verified, _) = verify(net)
        self.assertFalse(verified)

    def test_net_will_verify_bl1(self):
        for _ in range(0, 5):
            net = create_net()
            train_and_check(net)

            (verified, _) = verify(net, factor=0.85)
            if verified:
                break
        self.assertTrue(verified)

    def test_net_will_verify_bl2(self):
        for _ in range(0, 5):
            net = create_net()
            train_and_check(net, league='bl2')

            (verified, _) = verify(net, league='bl2', factor=0.85)
            if verified:
                break
        self.assertTrue(verified)

    def test_net_will_predict_each(self):
        net = create_net()
        result = train_and_check(net)
        stats = result.get_statistics()

        self.assertGreater(stats[0], 1)
        self.assertGreater(stats[1], 1)
        self.assertGreater(stats[2], 1)

    def test_calculate_points_empty_stats_no_verify(self):
        stats = QueryStatistics()
        points = calculate_points(stats, 0)
        self.assertEquals(points, 0)

    def test_calculate_points_empty_stats_with_verify(self):
        stats = QueryStatistics()
        points = calculate_points(stats, 9)
        self.assertEquals(points, 9)

    def test_calculate_points_mid_performance(self):
        stats = QueryStatistics()
        stats.count = 100
        stats.hits = 52
        points = calculate_points(stats, 0)
        self.assertEquals(points, 104)

    def test_calculate_points_full_performance(self):
        stats = QueryStatistics()
        stats.count = 300
        stats.hits = 300
        points = calculate_points(stats, 0)
        self.assertEquals(points, 200)

    def test_calculate_points_performance_with_verify(self):
        stats = QueryStatistics()
        stats.count = 200
        stats.hits = 164
        points = calculate_points(stats, 3)
        self.assertEquals(points, 167)

    def test_calculate_points_2expecy_equals_1verify(self):
        stats = QueryStatistics()
        stats.count = 100
        stats.hits = 50
        stats.win = 98
        points1 = calculate_points(stats, 1)
        stats.win = 100
        points2 = calculate_points(stats, 0)
        self.assertEquals(points1, points2)

if __name__ == '__main__':
    unittest.main()
