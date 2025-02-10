import numpy as np
import test_binary

def test_permutation(M) -> bool:
    return test_binary.test_binary(M) and np.linalg.norm(np.dot(M.T, M) - np.eye(M.shape[0]), 1) == 0