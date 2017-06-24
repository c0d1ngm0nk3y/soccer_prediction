import unittest
import numpy
from NeuralNetwork import NN, NN2


class NeuralNetworkTests(unittest.TestCase):
    def test_simple(self):
        net = NN(3, 3, 2)
        result = net.query([0.5, 1, 0])

        self.assertEqual(2, len(result))


    def test_activate_function(self):
        net = NN2(3, 100, 2)
        result = net.query([0.5, 1, 0]).flatten()

        self.assertTrue(max(result) <= 1)
        self.assertTrue(min(result) >= 0)


    def test_simple_train(self):
        net = NN2(3, 100, 2)
        (result, _) = net.train([0.5, 1, 0], [0.5, 0.5])

        self.assertTrue(max(result) <= 1)
        self.assertTrue(min(result) >= 0)

    def test_train_improves(self):
        net = NN2(3, 100, 2)
        (out1, err1) = net.train([0.5, 1, 0], [0.5, 0.5])
        (out2, err2) = net.train([0.5, 1, 0], [0.5, 0.5])

        self.assertFalse(numpy.array_equal(out1, out2))
        self.assertFalse(numpy.array_equal(err1, err2))
        self.assertGreater(max(abs(err1)), max(abs(err2)))


    def test_simple_can_be_learned(self):
        net = NN2(3, 100, 2)

        for x in range(0, 50):
            (out, err) = net.train([0.5, 1, 0], [0.5, 0.5])

        self.assertGreater(0.1, max(abs(err)))

if __name__ == '__main__':
    unittest.main()
