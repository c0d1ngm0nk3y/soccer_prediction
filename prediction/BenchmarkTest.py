from __future__ import absolute_import
import unittest
from prediction.Benchmark import verify
from prediction.NetTrainer import PickAway, create_net, train_and_check


class BenchmarkTest(unittest.TestCase):
    def test_pick_leader_will_not_verify(self):
        net = PickAway()
        verified = verify(net)
        self.assertFalse(verified)

    def test_default_net_will_verify(self):
        for _ in range(0, 3):
            net = create_net()
            train_and_check(net)

            verified = verify(net, factor=0.8, debug=False)
            if verified:
                break
        self.assertTrue(verified)

    def test_default_net_will_predict_each(self):
        net = create_net()
        (_, _, _, stats) = train_and_check(net)

        self.assertGreater(stats[0], 1)
        self.assertGreater(stats[1], 1)
        self.assertGreater(stats[2], 1)

if __name__ == '__main__':
    unittest.main()
