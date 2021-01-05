class Perceptron:
    size = int(0)
    bias = int(0)
    weight = []

    def __init__(self, size: int):
        self.size = size
        self.weight = [0 for _ in range(size)]

    def get_weights(self):
        return self.weight
