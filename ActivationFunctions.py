# E var I am tried of copying it
e = 2.7182818284590452353602874713526624


def sigmoid(x: float) -> float:
    """
    Calculate sigmoid function
    :param x: Input to the sigmoid function
    :return: Value computed by the sigmoid function
    """
    return 1 / (1 + (e ** (-x)))


def sigmoid_prime(x: float) -> float:
    """
    Calculate the prime of the sigmoid function
    :param x: Number to apply the prime sigmoid function
    :return: Value of the prime sigmoid
    """
    return (e ** x) / ((1 + (e ** x)) ** 2)


def relu(x: float) -> float:
    """
    Relu activation function
    :param x: Number to apply the activation function
    :return: Value after relu
    """
    return max(0.0, x)


def relu_prime(x: float) -> float:
    """
    Calculate the the prime of the relu function
    :param x: Number to apply the prime relu function
    :return: Value of the prime relu
    """
    if x > 0:
        return 1
    return 0


# Dictionary of activation functions
functionList = {
    "sigmoid": [sigmoid, sigmoid_prime],
    "relu": [relu, relu_prime]
}
