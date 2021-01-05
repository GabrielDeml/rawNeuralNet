from FakeNumpy import *


class Perceptron:
    size = int(0)
    bias = int(0)
    weights = []

    def __init__(self, size: int):
        self.size = size
        self.weights = create_zero_matrix(size)

    def get_weights(self) -> list:
        return self.weights

    def calculate_perceptron(self, data_in: list):
        return matrix_add(element_multiply(data_in, self.weights), self.bias)
