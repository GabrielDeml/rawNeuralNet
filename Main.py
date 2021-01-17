#!/usr/bin/env python3
from Activation import Activation
from Perceptron import Perceptron
from MatrixMath import *
from Support import *

# Generate fake data
trainingData = list(range(100))
labels = matrix_generic(list(range(100)), lambda a: a ** 2)

# Training values
epochs = 5

if __name__ == "__main__":
    print(trainingData)
    print(labels)

    # Create the model
    model = [
        Perceptron(1, 1),
        Activation("relu")
    ]

    # Check that the size of the data and labels match
    if len(trainingData) != len(labels):
        raise Exception("Data and labels do not match")

    # For each epoch
    for i in range(epochs):
        # For each data point
        for dataPoint in range(len(trainingData)):
            out = trainingData[dataPoint]
            for layer in model:
                out = layer.forward_propagation(out)
