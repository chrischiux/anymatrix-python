import rogues.matrices.hankel as rogues_hankel
import numpy as np

def hankel(a, b=None):
    """
    hankel(a) returns a toeplitz matrix given "a", the first row of the
    matrix.  This matrix is defined as:

         [[   a[0], a[1], a[2], a[3], ..., a[n-1], a[n] ]]
          [   a[1], a[2], a[3], a[4], ...,   a[n],   0  ]
          [   a[2], a[3], a[4], ...,     ]
          ...
          [ a[n-2], a[n-1], a[n],  0,   ...
          [ a[n-1], a[n],      0,  0,   ...           0
          [   a[n],    0,      0,  0,   ...           0 ] ]


    Note that all the non-zero anti-diagonals are constant

    If called as hankel(a, b) then create the hankel matrix where a is the
    first column and b is the last row.  If a[-1] != b[0], a[-1] is chosen
    but a warning message is printed.  For example

    >>> import numpy as np
    >>> from rogues import hankel
    >>> a = np.arange(10)
    >>> b = np.arange(10,20)
    >>> h = hankel(a, b)
    Warning: a[-1] != b[0]. a[-1] is chosen
    >>> h
    array([[ 0,  1,  2,  3,  4,  5,  6,  7,  8,  9],
           [ 1,  2,  3,  4,  5,  6,  7,  8,  9, 11],
           [ 2,  3,  4,  5,  6,  7,  8,  9, 11, 12],
           [ 3,  4,  5,  6,  7,  8,  9, 11, 12, 13],
           [ 4,  5,  6,  7,  8,  9, 11, 12, 13, 14],
           [ 5,  6,  7,  8,  9, 11, 12, 13, 14, 15],
           [ 6,  7,  8,  9, 11, 12, 13, 14, 15, 16],
           [ 7,  8,  9, 11, 12, 13, 14, 15, 16, 17],
           [ 8,  9, 11, 12, 13, 14, 15, 16, 17, 18],
           [ 9, 11, 12, 13, 14, 15, 16, 17, 18, 19]])
    """
    if type(a) is int or type(a) is float:
        return np.array([[a]])
    if type(a) is np.ndarray and a.ndim == 1:
        return np.array([a])
    # Convert to numpy arrays if not already
    if type(a) is not np.ndarray:
        a = np.array(a)
    if b is not None and type(b) is not np.ndarray:
        b = np.array(b)
    return rogues_hankel(a,b)