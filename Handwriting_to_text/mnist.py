from packaging import version
import sklearn
import sys
import tensorflow as tf
import matplotlib.pyplot as plt
from pathlib import Path
import numpy as np


"""Loading dataset"""
mnist = tf.keras.datasets.mnist.load_data()
(X_train_full, y_train_full), (X_test, y_test) = mnist
X_train, y_train = X_train_full[:-5000], y_train_full[:-5000]
X_valid, y_valid = X_train_full[-5000:], y_train_full[-5000:]

"""Normalizing the data"""
X_train, X_valid, X_test = X_train / 255., X_valid / 255., X_test / 255.

"""Showing an image from the dataset"""
# plt.imshow(X_train[0], cmap="binary")
# plt.axis('off')
# plt.show()

"""Creating the model, using Sequential API"""
tf.random.set_seed(42)
model = tf.keras.Sequential()
model.add(tf.keras.layers.InputLayer(input_shape=[28, 28]))
model.add(tf.keras.layers.Flatten())
model.add(tf.keras.layers.Dense(300, activation="relu"))
model.add(tf.keras.layers.Dense(100, activation="relu"))
model.add(tf.keras.layers.Dense(10, activation="softmax"))

# print(model.summary())
# tf.keras.utils.plot_model(model, "my_mnist_model.png", show_shapes=True)
hidden1 = model.layers[1]
# print(hidden1.name)

"""Compiling the model"""
model.compile(loss="sparse_categorical_crossentropy", optimizer="sgd", metrics=["accuracy"])

np.argmax(
    [[0., 0., 0., 0., 0., 0., 0., 1., 0., 0.],
     [0., 0., 0., 0., 0., 0., 0., 0., 1., 0.],
     [0., 0., 0., 0., 0., 0., 0., 0., 0., 1.],
     [1., 0., 0., 0., 0., 0., 0., 0., 0., 0.]],
    axis=1
)

history = model.fit(X_train, y_train, epochs=30, validation_data=(X_valid, y_valid))

test_loss, test_accuracy = model.evaluate(X_test, y_test)
print(f"Test accuracy: {test_accuracy:.2f}")
