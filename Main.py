#!/usr/bin/env python3
from Activation import Activation
from ErrorFunctions import mean_square_error
from Perceptron import Perceptron
from MatrixMath import *
from Support import *

# Generate fake data
trainingData, labels = generate_dataset(100)
# trainingData = labels

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
        error = 0
        # For each data point
        for dataPoint in range(len(trainingData)):
            out = trainingData[dataPoint]
            label = labels[dataPoint]
            for layer in model:
                out = layer.forward_propagation(out)
            error += mean_square_error(out[0], label)
