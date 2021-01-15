#!/usr/bin/env python3
from Perceptron import Perceptron
from Support import *
from MatrixMath import *
from ActivationFunctions import *

data = list(range(100))
labels = matrix_generic(list(range(100)), lambda a: a**2)

perceptron = Perceptron(3, 2)


if __name__ == "__main__":
    model = [

    ]
