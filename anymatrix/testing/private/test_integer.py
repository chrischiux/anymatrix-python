import numpy as np

def test_integer(M):
    return not np.any(np.remainder(M, 1))