import os


def random_int() -> int:
    """
    Creates a random number between 0 and 9
    :return: A random int between 0 and 9
    """
    # Magic number 255/10 = 25.5
    with open("/dev/urandom", 'rb') as f:
        return int(int.from_bytes(f.read(1), 'big') / 25.5)


def get_digit(number: int, n: int) -> int:
    """
    Gets the nth digit
    :param number: Number to get the digit from
    :param n: The location of the digit to get
    :return: The nth digit that was gotten
    """
    return number // 10 ** n % 10


def dot_vector(vector1: list, vector2: list) -> int:
    """
    Take the dot product of the two 2d vectors
    :param vector1: First vector
    :param vector2: Second vector
    :return: Dot product of the two vectors
    """
    # Make sure the length of the vectors are the same
    if len(vector1) != len(vector2):
        raise Exception("Vectors must have the same length for dot product")
    return sum(
        (vector1[_] * vector2[_])
        for _ in range(len(vector1))
    )


def element_multiply(matrix1: list, matrix2: list) -> list:
    """
    Do element multiplication on a matrix
    :param matrix1: First matrix
    :param matrix2: Second matrix
    :return: The result of the elementwise multiplication
    """
    if len(matrix1) != len(matrix2):
        raise Exception("Matrices size must match to do element multiplication")
    out_matrix = []
    for i in range(len(matrix1)):
        if isinstance(matrix1[i], list) & isinstance(matrix2[i], list):
            out_matrix.append(element_multiply(matrix1[i], matrix2[i]))
        else:
            out_matrix.append(matrix1[i] * matrix2[i])
    return out_matrix


def pretty_print(matrix: list) -> None:
    """
    Print a matrix or a vector in a pretty way
    :param matrix: Matrix to print
    :return: None
    """
    # For every element in the list
    for i in matrix:
        # Check if it is a list
        # If it is print everything in that list
        if isinstance(i, list):
            for j in i:
                print(j, end=" ")
        # Print that element of the list
        else:
            print(i)
        # Add a new line
        print()


def create_zero_matrix(size: int) -> list:
    """
    Create a matrix of size x filled with zeros
    :param size: Size to make the matrix
    :return: The matrix created
    """
    rows = [0 for _ in range(size)]
    return [rows for _ in range(size)]
