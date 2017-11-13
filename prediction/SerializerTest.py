from __future__ import absolute_import
import unittest
from prediction.Serializer import save_net, load_net, as_string, from_string
from prediction.NetTrainer import create_net, train_and_check


class SerializerTest(unittest.TestCase):
    def test_after_serialize_same(self):
        net1 = create_net()
        result1 = train_and_check(net1)

        string = as_string(net1)
        net2 = from_string(string)

        result2 = train_and_check(net2, train_set=[])

        self.assertEqual(result1.get_performance(), result2.get_performance())

    def test_save_load_from_file(self):
        net1 = create_net()
        result1 = train_and_check(net1)

        filename = './prediction/pickles/test.pickle'
        save_net(net1, filename)
        net2 = load_net(filename)

        result2 = train_and_check(net2, train_set=[])

        self.assertEqual(result1.get_performance(), result2.get_performance())


if __name__ == '__main__':
    unittest.main()
