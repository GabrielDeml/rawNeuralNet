class Perceptron:
    size = 0
    bias = 0
    weight = 0

    def __init__(self, size):
        self.size = size
        self.weight = [0 for _ in range(size)]

    def Print_Weights(self):
        print("hello")
        print(self.weight)