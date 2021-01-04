import os


def random_int() -> int:
    """ Returns a random int

    Returns:
        int: The random int generated

    """
    with open("/dev/urandom", 'rb') as f:
        return int(int.from_bytes(f.read(1), 'big') / 25.5)


def get_digit(number: int, n: int) -> int:
    """ Returns the nth number in the integer

    Args:
        number (int): Number to take the n digit from
        n (int): location of n to take the number from

    Returns:
        int: Number taken from the orginal number

    """
    return number // 10 ** n % 10


def dot2d(matrix1: list, matrix2: list) -> int:
    out_list = int(0)
    if len(matrix1) == len(matrix2):
        out_list = sum(
            (matrix1[pointer] * matrix2[pointer])
            for pointer in range(len(matrix1))
        )
    return out_list
