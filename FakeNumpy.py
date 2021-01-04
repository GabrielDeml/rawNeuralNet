import os


def random_int() -> int:
    """
    Creates a random number between 0 and 9
    :return: A random int between 0 and 9
    """
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


def dot2d(matrix1: list, matrix2: list) -> int:
    """
    Take the dot product of the two 2d matrixes
    :param matrix1: First matrix
    :param matrix2: Second matrix
    :return: Dot product of the two matrixes
    """
    out_list = int(0)
    if len(matrix1) == len(matrix2):
        out_list = sum(
            (matrix1[pointer] * matrix2[pointer])
            for pointer in range(len(matrix1))
        )
    return out_list
