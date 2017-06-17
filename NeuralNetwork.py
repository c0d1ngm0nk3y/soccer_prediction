import numpy
import scipy.special

class NN(object):
    def __init__(self, i_size, h_size, o_size, alpha=0.1):
        self.alpha = alpha
        self.i_size = i_size
        self.h_size = h_size
        self.o_size = o_size
        self.w1 = None
        self.w2 = None
        self.init_weights()
        pass

    def init_weights(self):
        self.w1 = numpy.random.rand(self.h_size, self.i_size) - 0.5
        self.w2 = numpy.random.rand(self.o_size, self.h_size) - 0.5

    def activate_function(self, x):
        return scipy.special.expit(x)

    def query(self, input_list):
        (result, _) = self.train(input_list, None)
        return result

    def train(self, input_list, target_list):
        input = numpy.array(input_list, ndmin=2).T
        h_input = numpy.dot(self.w1, input)
        h_output = self.activate_function(h_input)

        final_input = numpy.dot(self.w2, h_output)
        final_output = self.activate_function(final_input)

        if not target_list:
            return (final_output, None)

        target = numpy.array(target_list, ndmin=2).T
        errors = target - final_output
        h_errors = numpy.dot(self.w2.T, errors)

        delta_w2 = self._calculate_delta_weights(errors, final_output, h_output)
        self.w2 += delta_w2

        delta_w1 = self._calculate_delta_weights(h_errors, h_output, input)
        self.w1 += delta_w1

        return (final_output, errors)

    def _calculate_delta_weights(self, errors, output, prev_output):
        delta_w = self.alpha * numpy.dot((errors * output * (1.0 - output)), numpy.transpose(prev_output))
        return delta_w

class  NN2(NN):
    def init_weights(self):
        self.w1 = numpy.random.normal(0.0, pow(self.h_size, -0.5), (self.h_size, self.i_size))
        self.w2 = numpy.random.normal(0.0, pow(self.o_size, -0.5), (self.o_size, self.h_size))
