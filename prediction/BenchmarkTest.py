from __future__ import absolute_import
import unittest
from prediction.Benchmark import verify
from prediction.NetTrainer import PickAway, create_net, train_and_check


class BenchmarkTest(unittest.TestCase):
    def test_PickAway_will_not_verify(self):
        net = PickAway()
        verified = verify(net)
        self.assertFalse(verified)

    def test_default_net_will_verify_in_3_tries(self):
        for i in range(0, 3):
            net = create_net()
            train_and_check(net)

            verified = verify(net)
            if verified:
                break
        self.assertTrue(verified)


if __name__ == '__main__':
    unittest.main()
