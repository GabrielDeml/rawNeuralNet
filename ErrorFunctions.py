def mean_square_error(x: list, y: list) -> float:
    """
    Calculate mean square error
    :param x: First matrix
    :param y: Second matrix
    :return: Mean square error
    """
    if len(x) != len(y):
        raise Exception("Input matrices must be the same size")
    return sum((x[i] - y[i]) ** 2 for i in range(len(x))) / len(x)
