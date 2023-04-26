import math
import matplotlib.pyplot as plt
import random
from collections import Counter
import numpy as np
from statistics import mean


class Point:

    def __init__(self, coords, f):
        if type(coords) == int:  # Number of coordinates specified
            self.coords = [random.random() for _ in range(coords)]
        else:  # Sequence of coordinates specified
            self.coords = coords
        self.target = f(self.coords)

    def __str__(self):
        return f'{self.coords} -> {self.target}'

    def __repr__(self):
        return str(self)

    def distance_to(self, other):
        squared_differences = [(a-b)**2 for a, b in zip(self.coords, other.coords)]
        return math.sqrt(sum(squared_differences))


def f1(coords):
    x, y = coords
    return y > -0.5 + 2 * x

def f2(coords):
    center = Point([0.5 for _ in coords], max)
    # p = Point([x for x in coords], max)
    p = Point([x + random.gauss(0, 0.1) for x in coords], max)
    return 0.25 < p.distance_to(center) < 0.5

def plot(dataset, k):
    # Plot the classifier's boundary in the background
    xs = []
    ys = []
    zs = []
    for x in np.linspace(0, 1, 100):
        for y in np.linspace(0, 1, 100):
            coords = (x, y)
            prediction = knn_classify(k, train, Point(coords, max))
            xs.append(x)
            ys.append(y)
            zs.append(prediction)
    plt.scatter(xs, ys, c=zs, alpha=0.5, s=2)

    # Plot the training points
    def plot_subset(subset, symbol):
        xs = [p.coords[0] for p in subset]
        ys = [p.coords[1] for p in subset]
        plt.scatter(xs, ys, marker=symbol, color='black')
    plot_subset([p for p in dataset if p.target], 'o')
    plot_subset([p for p in dataset if not p.target], 'x')
    # Show the result
    plt.show()


def knn_classify(k, train, p):
    '''
    :param k: The number of neighbors to consider.
    :param train: A sequence of Points.
    :param p: The point whose target is to be predicted.
    :return: The k-nearest-neighbors prediction for the target of p.
    '''
    nearest = sorted(train, key=p.distance_to)[:k]
    winner, _ = Counter(p.target for p in nearest).most_common(1)[0]
    return winner


def accuracy(k, train, test):
    return mean(knn_classify(k, train, p) == p.target for p in test)


train = [Point(2, f2) for _ in range(500)]
test = [Point(2, f2) for _ in range(500)]

train_accuracy = [accuracy(k, train, train) for k in range(1, 100, 2)]
test_accuracy = [accuracy(k, train, test) for k in range(1, 100, 2)]

plt.plot(train_accuracy, label='Training set')
plt.plot(test_accuracy, label='Test set')
plt.xlabel('k')
plt.ylabel('accuracy')
plt.legend()
plt.show()