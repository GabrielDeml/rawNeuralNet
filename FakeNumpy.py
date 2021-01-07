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


def matrix_dot(matrix1: list, matrix2: list) -> int:
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
    if len(matrix1) != len(matrix2):
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


def create_n_matrix(size: int, n: int) -> list:
    """
    Create a matrix of size x filled with n
    :param size: Size of the matrix
    :param n: The value to fill the matrix with
    :return: The matrix created
    """
    return [[n for _ in range(size)] for _ in range(size)]


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
