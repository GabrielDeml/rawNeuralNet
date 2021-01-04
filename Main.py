#!/usr/bin/env python
from Perceptron import Perceptron
from FakeNumpy import FakeNumpy

data = {1,2,3,4,5}
labels = {1,2,3,4,5}

perceptron = Perceptron(10)
fakeNumpy = FakeNumpy()

if __name__ == "__main__":
    print(perceptron.Get_Weights())
    print(fakeNumpy.randomInt())
        