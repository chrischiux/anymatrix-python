import numpy as np
def test_positive(M):
    if np.all((M > 0)) == np.True_:
        return True
    else:
        return False