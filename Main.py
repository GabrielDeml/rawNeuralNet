#!/usr/bin/env python3
from Perceptron import Perceptron
from Support import *
from MatrixMath import *
from ActivationFunctions import *

data = list([1, 2, 3, 4, 5])
labels = list([1, 2, 3, 4, 5])
data2 = list([[1, 2], [3, 4], [5, 6], [7, 8], [9, 10]])

perceptron = Perceptron(3, 2)
# fakeNumpy = FakeNumpy()

if __name__ == "__main__":
    # print(perceptron.get_weights())
    # print(random_int())
    # print(data2)
    # print(dot_vector([2, 2], [1, 1]))
    # print(element_multiply([[2, 2], [2, 2]], [[1, 2], [1, 2]]))
    # pretty_print([[2, 3], [2, 1]])
    # pretty_print([1])
    # pretty_print(create_zero_matrix(2))
    # pretty_print(create_n_matrix(2, 1))
    # pretty_print(matrix_add([1], 2))
    # perceptron.weights = create_n_matrix(2, 1)
    # pretty_print(perceptron.calculate_perceptron(create_n_matrix(3, 1)))
    # print(matrix_dot([2, 2], [2, 2]))
    # pretty_print(create_n_matrix(5, 4, random_int))
    # print("==================")
    # pretty_print(transpose(matrix))
    # print(sigmoid(2))
    print(sigmoid_prime(2))
