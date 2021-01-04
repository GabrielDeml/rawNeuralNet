#!/usr/bin/env python3
from Perceptron import Perceptron
from FakeNumpy import *

data = list([1, 2, 3, 4, 5])
labels = list([1, 2, 3, 4, 5])
data2 = list([[1, 2], [3, 4], [5, 6], [7, 8], [9, 10]])

perceptron = Perceptron(10)
# fakeNumpy = FakeNumpy()

if __name__ == "__main__":
    print(perceptron.get_weights())
    print(random_int())
    print(data2)
    print(dot2d([2, 2], [1]))
