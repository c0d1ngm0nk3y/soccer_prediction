#encoding=utf8
import unittest
from prediction.NetTrainer import create_net, train_and_check
from prediction.Benchmark import verify

class NetCreationTest(unittest.TestCase):
    def test_home_and_away_nets(self):
        max_delta=45
        a_net = create_net()
        stats = train_and_check(a_net, train_set=['2015', '2016'], league='bl1', check='2017')
        (verified, verified_result) = verify(a_net, league='bl1', delta=max_delta)

        self.assertEqual(stats.get_count(), 216)
        self.assertGreater(verified_result, -max_delta)
        self.assertTrue(verified)


if __name__ == '__main__':
    unittest.main()
