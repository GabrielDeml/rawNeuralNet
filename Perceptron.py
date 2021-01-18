from Support import *
from ActivationFunctions import *
from MatrixMath import *


class Perceptron:
    size_in = 0
    size_out = 0
    weights = []
    bias = []
    data_in = 0

    def __init__(self, size_in: int, size_out: int):
        """
        Init Perceptron
        :param size_in: Number of input neurons
        :param size_out: Number of output neurons
        """
        self.size_in = size_in
        self.size_out = size_out
        self.weights = create_n_matrix(size_in, size_out, random_int)
        self.bias = create_n_vector(size_out, random_int)

    def get_weights(self) -> list:
        """
        Get the weights of the perceptron
        :return: The weight of the perceptron
        """
        return self.weights

    def forward_propagation(self, data_in: list) -> list:
        """
        Calculate the output of a perceptron
        :param data_in: Input data to the perceptron
        :return: The output of the perceptron
        """
        self.data_in = data_in
        return [[matrix_dot(data_in, self.weights) + n] for n in self.bias]

    def backpropagation(self, out_error: list, learning_rate: float):
        """
        Calculate backpropagation
        :param out_error: Error from the last layer
        :param learning_rate: Rate for the network to learn
        :return: Error of the next layer
        """
        in_error = matrix_dot(out_error, transpose(self.weights))
        weights_error = matrix_dot(transpose(self.data_in), out_error)

        self.weights -= learning_rate * weights_error
        self.bias -= matrix_generic(out_error, lambda a: a * learning_rate)
        return in_error
