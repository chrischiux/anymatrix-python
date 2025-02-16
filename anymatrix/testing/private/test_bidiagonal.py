import numpy as np

def test_bidiagonal(M):
    return np.array_equal(M, np.triu(np.tril(M, 1))) or np.array_equal(M, np.triu(np.tril(M), -1))