import numpy as np
def vander(p):
    """
    VAND   Vandermonde matrix.
        Produced useing np.vander when p is a vector, and 1 when p is an int or float.
    """
    if p == int or p == float:
        return 1
    else:
        return np.vander(p)

