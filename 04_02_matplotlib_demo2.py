import matplotlib.pyplot as plt
import numpy as np


def sigmoid(x):
    return 1.0 / (1 + np.exp(-x))


a = np.linspace(-10, 10, 1000)
plt.hold(True)
plt.plot(a, sigmoid(a))
plt.plot(a, sigmoid(a) * (1 - sigmoid(a)))

plt.show()
