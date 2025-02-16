import numpy as np
def test_binary(M):
    if np.all((M == 0) | (M == 1)) == np.True_:
        return True
    else:
        return False