import numpy
import scipy.special


class NN(object):
    def __init__(self, i_size, h_size, o_size, alpha=0.1):
        self.alpha = alpha
        self.i_size = i_size
        self.h_size = h_size
        self.o_size = o_size
        self.weight1 = None
        self.weight2 = None
        self.init_weights()

    def init_weights(self):
        self.weight1 = numpy.random.rand(self.h_size, self.i_size) - 0.5
        self.weight2 = numpy.random.rand(self.o_size, self.h_size) - 0.5

    def activate_function(self, x):
        return scipy.special.expit(x)

    def query(self, input_list):
        (result, _) = self.train(input_list, None)
        return result

    def train(self, input_list, target_list):
        input_array = numpy.array(input_list, ndmin=2).T
        h_input = numpy.dot(self.weight1, input_array)
        h_output = self.activate_function(h_input)

        final_input = numpy.dot(self.weight2, h_output)
        final_output = self.activate_function(final_input)

        if not target_list:
            return (final_output, None)

        target = numpy.array(target_list, ndmin=2).T
        errors = target - final_output
        h_errors = numpy.dot(self.weight2.T, errors)

        delta_w2 = self._calculate_delta_weights(errors, final_output, h_output)
        self.weight2 += delta_w2

        delta_w1 = self._calculate_delta_weights(h_errors, h_output, input_array)
        self.weight1 += delta_w1

        return (final_output, errors)

    def _calculate_delta_weights(self, errors, output, prev_output):
        transposed = numpy.transpose(prev_output)
        factor = errors * output * (1.0 - output)
        delta_w = self.alpha * numpy.dot(factor, transposed)
        return delta_w

class  NN2(NN):
    def init_weights(self):
        self.weight1 = numpy.random.normal(0.0, pow(self.h_size, -0.5), (self.h_size, self.i_size))
        self.weight2 = numpy.random.normal(0.0, pow(self.o_size, -0.5), (self.o_size, self.h_size))
