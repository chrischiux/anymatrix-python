import rogues.matrices.hankel as rogues_hankel
import numpy as np

def hankel(a, b=None):

    if type(a) is int or type(a) is float:
        return np.array([[a]])
    if type(a) is np.ndarray and a.ndim == 1:
        return np.array([a])
    # Convert to numpy arrays if not already
    if type(a) is not np.ndarray:
        a = np.array(a)
    if b is not None and type(b) is not np.ndarray:
        b = np.array(b)
    return rogues_hankel(a,b)

# Copy docstring from original function
hankel.__doc__ = rogues_hankel.__doc__