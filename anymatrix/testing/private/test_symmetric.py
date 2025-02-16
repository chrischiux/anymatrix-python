import numpy as np

def test_symmetric(M):
    return np.allclose(M, M.T)
