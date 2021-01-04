#!/usr/bin/env python
from Perceptron import Perceptron
from FakeNumpy import FakeNumpy

data = [1,2,3,4,5]
labels = [1,2,3,4,5]
data2 = [[1,2], [3,4],[5,6],[7,8],[9,10]]

perceptron = Perceptron(10)
fakeNumpy = FakeNumpy()

if __name__ == "__main__":
    print(perceptron.get_weights())
    print(fakeNumpy.random_int())
    print(data2)
        