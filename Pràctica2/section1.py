import numpy as np
import sklearn.datasets
import matplotlib.pyplot as plt

class Section1:
    def __init__(self):
        self.X = None
        self.Y = None

    def load_data(self):
        digits = sklearn.datasets.load_digits()
        self.X = digits.data
        self.Y = digits.target

    def analyze_data(self):
        print(f"Data X, Y: {self.X.shape}, {self.Y.shape}\n")
        print(f"Mean:\n{np.mean(self.X, axis=0)}")
        print(f"Standard deviation:\n{np.std(self.X, axis=0)}\n")
        print(f"Number of samples per class: {np.bincount(self.Y)}\n")

        for i in range(10):
            plt.figure()
            plt.imshow(np.mean(self.X[self.Y == i, :], axis=0).reshape(8, 8))
            plt.title(f"Digit {i}")
            print(f"The STD accumulated for digit {i} is {np.std(self.X[self.Y == i, :])}")

    def run_all(self):
        self.load_data()
        self.analyze_data()