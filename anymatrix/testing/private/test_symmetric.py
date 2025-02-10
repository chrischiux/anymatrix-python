import numpy as np

def test_symmetric(M):
    return np.array_equal(M, M.T)