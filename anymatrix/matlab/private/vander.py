import numpy as np
def vander(p):
    """
    VAND   Vandermonde matrix.
       Produced useing np.vander
    """
    if p == int or p == float:
      return 1
    else:
      return np.vander(p)