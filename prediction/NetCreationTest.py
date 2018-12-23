#encoding=utf8
import unittest
from prediction.NetTrainer import create_net, train_and_check, NetTrainer
from prediction.Benchmark import verify
from prediction.Judger import HomeAwayJudger, HomeJudger, AwayJudger

class NetCreationTest(unittest.TestCase):
    def test_home_and_away_net(self):
        max_delta = 45
        a_net = create_net()
        judger = HomeAwayJudger()
        trainer = NetTrainer(a_net, judger)

        stats = train_and_check(a_net, train_set=['2015', '2016'], league='bl1', check='2017', trainer=trainer)
        print stats
        (verified, verified_result) = verify(a_net, league='bl1', delta=max_delta)

        self.assertEqual(stats.get_count(), 216)
        self.assertGreater(verified_result, -max_delta)
        self.assertLess(verified_result, -5)
        self.assertTrue(verified)

    def test_only_home_net(self):
        max_delta = 60
        a_net = create_net(output_layer=1)

        judger = HomeJudger()
        trainer = NetTrainer(a_net, judger)

        stats = train_and_check(a_net, train_set=['2015', '2016'], league='bl1', check='2017', trainer=trainer)
        print stats
        (verified, verified_result) = verify(a_net, league='bl1', delta=max_delta, trainer=trainer)

        self.assertEqual(stats.get_count(), 216)
        self.assertGreater(verified_result, -max_delta)
        self.assertTrue(verified)

    def test_only_away_net(self):
        max_delta = 60
        a_net = create_net(output_layer=1)

        judger = AwayJudger()
        trainer = NetTrainer(a_net, judger)

        stats = train_and_check(a_net, train_set=['2015', '2016'], league='bl1', check='2017', trainer=trainer)
        print stats
        (verified, verified_result) = verify(a_net, league='bl1', delta=max_delta, trainer=trainer)

        self.assertEqual(stats.get_count(), 216)
        self.assertGreater(verified_result, -max_delta)
        self.assertTrue(verified)


if __name__ == '__main__':
    unittest.main()
