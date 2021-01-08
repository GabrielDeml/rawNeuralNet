from Support import *


class Perceptron:
    size = int(0)
    bias = int(0)
    weights = []

    def __init__(self, size: int):
        """
        Init Perceptron
        :param size: Size of the weight matrix
        """
        self.size = size
        # TODO: Make this the correct size
        self.weights = create_n_matrix(0, size, size)

    def get_weights(self) -> list:
        """
        Get the weights of the perceptron
        :return: The weight of the perceptron
        """
        return self.weights

    def calculate_perceptron(self, data_in: list):
        """
        Calculate the output of a perceptron
        :param data_in: Input data to the perceptron
        :return: The output of the perceptron
        """
        return sigmoid(matrix_dot(data_in, self.weights) + self.bias)
