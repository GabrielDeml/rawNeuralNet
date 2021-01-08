def sigmoid(x: float) -> float:
    """
    Calculate sigmoid function
    :param x: Input to the sigmoid function
    :return: Value computed by the sigmoid function
    """
    return 1 / (1 + (2.7182818284590452353602874713526624 ** (-x)))


def relu(x: float) -> float:
    """
    Relu activation function
    :param x: Number to apply the activation function
    :return: Value after relu
    """
    return max(0.0, x)