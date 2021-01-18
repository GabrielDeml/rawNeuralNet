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


def pretty_print(matrix: list) -> None:
    """
    Print a matrix or a vector in a pretty way
    :param matrix: Matrix to print
    :return: None
    """
    if isinstance(matrix, int):
        print(matrix)
        return
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


def create_n_matrix(width: int, height: int, n) -> list:
    """
    Create a matrix of size x filled with n
    :param width: Width of the matrix
    :param height: Height of the matrix
    :param n: The value to fill the matrix with or a function to generate a number
    :return: The matrix created
    """
    # If it is a function generate a matrix
    if callable(n):
        return [[n() for _ in range(width)] for _ in range(height)]
    # If it is a number generate a matrix
    return [[n for _ in range(width)] for _ in range(height)]


def create_n_vector(width: int, n) -> list:
    """
    Create a matrix of size x filled with n
    :param width: Width of the matrix
    :param n: The value to fill the matrix with or a function to generate a number
    :return: The matrix created
    """
    # If it is a function generate a vector
    if callable(n):
        return [n() for _ in range(width)]
    # If it is a number generate a vector
    return [n for _ in range(width)]


def generate_dataset(length: int):
    """
    Generate a dataset of i with labels i^2
    :param length: Length of the dataset
    :return: data and labels
    """
    return [[[i]] for i in range(length)], [[i] for i in range(length)]
