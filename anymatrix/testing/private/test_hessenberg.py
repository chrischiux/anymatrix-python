import numpy as np

def test_hessenberg(M):
    return np.array_equal(M, np.triu(M, -1)) or np.array_equal(M, np.tril(M, 1))