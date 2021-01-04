import os


class FakeNumpy:

    def get_digit(self, number : int, n : int) -> int:
        """ Returns the nth number in the integer

        Args:
            number (int): Number to take the n digit from
            n (int): location of n to take the number from

        Returns:
            int: Number taken from the orginal number

        """
        return number // 10**n % 10

    def random_int(self) -> int:
        """ Returns a random int

        Returns:
            int: The random int generated

        """
        with open("/dev/urandom", 'rb') as f:
            return int(int.from_bytes(f.read(1), 'big')/25.5)

    # def dot2D(self, matrix1 , matrix2):
    #     if()
