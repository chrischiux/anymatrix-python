import numpy as np

def test_stochastic(M):
    return np.linalg.norm(np.sum(M, axis=1) - 1, np.inf) < 10 * np.finfo(float).eps