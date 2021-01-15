def matrix_dot(matrix1: list, matrix2: list) -> float:
    """
    Take the dot product of the two 2d matrices
    :param matrix1: First matrix
    :param matrix2: Second matrix
    :return: Dot product of the two matrices
    """
    # Make sure the length of the matrices are the same
    if len(matrix1) != len(matrix2):
        raise Exception("Matrices must have the same length for dot product")
    out = 0
    for i in range(len(matrix1)):
        if isinstance(matrix1[i], list) & isinstance(matrix2[i], list):
            out += matrix_dot(matrix1[i], matrix2[i])
        else:
            out += matrix1[i] * matrix2[i]
    return out


def element_multiply(matrix1: list, matrix2: list) -> list:
    """
    Do element multiplication on a matrix
    :param matrix1: First matrix
    :param matrix2: Second matrix
    :return: The result of the elementwise multiplication
    """
    if len(matrix1) != len(matrix2) | len(matrix1[0]) != len(matrix2[0]):
        raise Exception("Matrices size must match to do element multiplication")
    out_matrix = []
    for i in range(len(matrix1)):
        if isinstance(matrix1[i], list) & isinstance(matrix2[i], list):
            out_matrix.append(element_multiply(matrix1[i], matrix2[i]))
        else:
            out_matrix.append(matrix1[i] * matrix2[i])
    return out_matrix


def matrix_add(matrix: list, n: int) -> list:
    """
    Do Addition on a matrix
    :param matrix: First matrix
    :param n: Number to add to the matrix
    :return: The result of the addition
    """
    out_matrix = []
    for item in matrix:
        if isinstance(item, list):
            out_matrix.append(matrix_add(item, n))
        else:
            out_matrix.append(item + n)
    return out_matrix


def matrix_generic(matrix: list, f: "Function to apply") -> list:
    """
    Do Addition on a matrix
    :param matrix: First matrix
    :param f: function to apply to the matrix
    :return: The result of the addition
    """
    out_matrix = []
    for item in matrix:
        if isinstance(item, list):
            out_matrix.append(matrix_add(item, f))
        else:
            out_matrix.append(f(item))
    return out_matrix


def transpose(x: list) -> list:
    """
    Transpose a matrix
    :param x: Matrix to transpose
    :return: Transposed matrix
    """
    if len(x) != len(x[0]):
        raise Exception("Matrices size must be square to do transpose.")
    return list(map(lambda *a: list(a), *x))
