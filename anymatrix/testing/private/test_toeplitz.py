import numpy as np
import rogues.utils.toeplitz as toeplitz

def test_toeplitz(M):
    return np.array_equal(toeplitz(M[:, 0], M[0, :]), M)