import numpy as np

def sigmoid(x):
    """
    Vectorized sigmoid function.
    """
    x = np.array(x)
    sigmoid_val = 1 / (1 + np.exp(-x))
    return sigmoid_val