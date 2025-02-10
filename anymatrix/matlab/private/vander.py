import numpy as np
def vander(p):
    """
    VAND   Vandermonde matrix.
       Produced useing np.vander
    """
    if type(p) is int or type(p) is float:
      return 1
    else:
      return np.vander(p)