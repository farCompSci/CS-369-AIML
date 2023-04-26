import math
import random
from statistics import mean
import matplotlib.pyplot as plt


class Point:
    def __init__(self, coords, f):
        if type(coords) == int:  # Number of coordinates specified
            self.coords = [random.random() for _ in range(coords)]
        else:  # Sequence of coordinates specified
            self.coords = coords
        self.target = f(self.coords)

    def __str__(self):
        return f'{self.coords} -> {self.target}' # String Representation of coords and targer

    def __repr__(self): # String representation of the object
        return str(self)

    def distance_to(self, other): # Calculating the distance between the point and a target
        squared_differences = [(a-b)**2 for a, b in zip(self.coords, other.coords)]
        return math.sqrt(sum(squared_differences))


def f3(coords): # Returns a function with noise
    x, y = coords
    r = math.sqrt(((x-0.3)*3)**2 + ((y-0.6)*3)**2)
    return (-math.sin(r) / r) + random.gauss(0, 0.1)


def f4(coords): # Also returns a function with noise
    x, y = coords
    def g(x1, y1, sigma):
        return (1 / (sigma * math.sqrt(2 * math.pi))) * math.exp(-(1 / (2 * sigma**2)) * ((x-x1)**2 + (y-y1)**2))
    return (-(g(0.1, 0.1, 0.1) + g(0.6, 0.7, 0.2) + g(0.5, 0.2, 0.12))) + random.gauss(0, 0.1)


def knn_regress(k, train, p):
    #Computes individual distances between the train values and p
    distances = [(train_point.distance_to(p), train_point.target) for train_point in train]
    #Sorts the distances found from descending to ascending order
    sorted_distances = sorted(distances)
    #Slice the part of the array for k number of values that we choose
    k_nearest = sorted_distances[:k]
    # Returns the mean of targets
    return mean(target for (distance, target) in k_nearest)


def mse(k, train, test):
    # Squared difference mean between target and predicted knn target in train
    train_mse = mean((p.target - knn_regress(k, train, p))**2 for p in train)
    # Squared difference mean between target and predicted knn target in test
    test_mse = mean((p.target - knn_regress(k, train, p))**2 for p in test)
    return train_mse, test_mse


def plot_mse(train, test, f):
    ks = range(1, 50, 2)
    train_mses = []
    test_mses = []
    for k in ks:
        train_mse, test_mse = mse(k, train, test)
        train_mses.append(train_mse)
        test_mses.append(test_mse)

    plt.plot(ks, train_mses, 'r-', label='Train')
    plt.plot(ks, test_mses, 'b-', label='Test')
    plt.legend()
    plt.xlabel('k')
    plt.ylabel('MSE')
    plt.title(f'MSE vs k for {f.__name__} function')
    plt.show()

def find_best_k(train, test):
    # finding the best k values using the train and test lists
    ks = range(1, 50, 2) # used to later iterate through the k values. Use steps of 2 to consider only odd values
    train_mses = [mean((p.target - knn_regress(k, train, p))**2 for p in train) for k in ks]
    test_mses = [mean((p.target - knn_regress(k, train, p))**2 for p in test) for k in ks]
    best_k_train = ks[train_mses.index(min(train_mses))]
    best_k_test = ks[test_mses.index(min(test_mses))]
    return best_k_train, best_k_test

# Create training and test sets for f3
f3_train = [Point(2, f3) for _ in range(500)]
f3_test = [Point(2, f3) for _ in range(500)]

# Create training and test sets for f4
f4_train = [Point(2, f4) for _ in range(500)]
f4_test = [Point(2, f4) for _ in range(500)]

# Finding the best k-values for f3 and f4
best_k_f3_train, best_k_f3_test = find_best_k(f3_train, f3_test)
best_k_f4_train, best_k_f4_test = find_best_k(f4_train,f4_test)
print(f'The best f3_train k: {best_k_f3_train} \nThe best f3_test k: {best_k_f3_test} \nThe best f4_train k: {best_k_f4_train} \nThe best f4_test k: {best_k_f4_test}')


# Set random seed for reproducibility
random.seed(0)

# Plot MSE vs k for f3
plot_mse(f3_train, f3_test, f3)

# Set random seed for reproducibility, if not set, random value will be chosen instead
random.seed(0)

# Plot MSE vs k for f4
plot_mse(f4_train, f4_test, f4)


# After running the  best_k function

# The best f3_train k: 1
# The best f3_test k: 11-19

# The best f4_train k: 1
# The best f4_test k: 5

# It does not matter whether we have the exact value for f3_test, as long as we are close
    # This is shown by the wavering of values when re-running the function

# For all the other values, it appears that all the k values are consistent, meaning the exact value matters for f3_ train, f4_train, and f4_test matter