import numpy as np
from numpy._core.numeric import (
    asanyarray, arange, zeros, greater_equal, multiply, ones,
    asarray, where, int8, int16, int32, int64, intp, empty, promote_types,
    diagonal, nonzero, indices
    )
def vander(x):
    """
    VAND   Vandermonde matrix.
       Produced useing np.vander
    """
    
    if type(x) is int or type(x) is float:
      return np.array([[1]])
    else:
      x = asarray(x)
      if x.ndim != 1:
          raise ValueError("x must be a one-dimensional array or sequence.")
      N = len(x)

      v = empty((len(x), N), dtype=promote_types(x.dtype, np.float64))
      tmp = v[:, ::-1]

      if N > 0:
          tmp[:, 0] = 1
      if N > 1:
          tmp[:, 1:] = x[:, None]
          multiply.accumulate(tmp[:, 1:], out=tmp[:, 1:], axis=1)

      return v