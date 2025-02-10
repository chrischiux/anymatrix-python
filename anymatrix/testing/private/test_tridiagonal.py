import numpy as np

def test_tridiagonal(M):
    return np.array_equal(M, np.tril(np.triu(M, -1), 1))