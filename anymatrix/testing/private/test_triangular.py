import numpy as np

def test_triangular(M):
    return np.allclose(M, np.tril(M)) or np.allclose(M, np.triu(M))