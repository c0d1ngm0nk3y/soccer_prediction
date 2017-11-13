from __future__ import absolute_import
import unittest
from prediction.Benchmark import verify
from prediction.NetTrainer import PickAway, create_net, train_and_check


class BenchmarkTest(unittest.TestCase):
    def test_pick_leader_wont_verify(self):
        net = PickAway()
        verified = verify(net)
        self.assertFalse(verified)

    def test_net_will_verify_bl1(self):
        for _ in range(0, 5):
            net = create_net()
            train_and_check(net)

            verified = verify(net, factor=0.85, debug=False)
            if verified:
                break
        self.assertTrue(verified)

    def test_net_will_verify_bl2(self):
        for _ in range(0, 5):
            net = create_net()
            train_and_check(net, league='bl2')

            verified = verify(net, league='bl2', factor=0.85, debug=False)
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

if __name__ == '__main__':
    unittest.main()
