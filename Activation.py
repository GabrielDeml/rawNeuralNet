from ActivationFunctions import *


class Activation:
    data_in = None

    def __init__(self, function: str) -> None:
        """
        Init for Activation
        :param function: String of activation function
        """
        self.forwardFunction = functionList[function][0]
        self.backwardFunction = functionList[function][1]

    def forward_propagation(self, data_in: list) -> list:
        """
        Forward propagation on the network
        :param data_in: data from the previous layer
        :return: output of the activation layer
        """
        self.data_in = data_in
        return [[self.forwardFunction(j) for j in i] for i in data_in]

    def backpropagation(self, error: float, rate) -> float:
        """
        Backward propagation on the network
        :param error: Error of the network
        :param rate: Place holder
        :return: Output of the backwards layer
        """
        return error * self.backwardFunction(self.data_in)
