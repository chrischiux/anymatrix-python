import numpy as np
def test_binary(M):
    return np.all((M == 0) | (M == 1))