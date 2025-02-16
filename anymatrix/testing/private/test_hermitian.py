import numpy as np

def test_hermitian(M: np.ndarray) -> bool:
    M = np.asmatrix(M)
    return np.allclose(M, M.H)