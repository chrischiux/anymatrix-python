import numpy as np
from scipy.special import comb
from math import sqrt

properties = ['symmetric', 'positive definite', 'integer',  'totally positive', 'infinitely divisible']

def beta(n, nargout=1):
    """BETA   Symmetric totally positive matrix of integers.
   BETA(n) is an n-by-n symmetric totally positive matrix of integers.
   It is also infinitely divisible.
   [A,R] = BETA(n) returns both the matrix and its explicitly constructed
   Cholesky factor R.

   Reference:
   P. Grover, V. S. Panwar and S. Reddy, Positivity Properties of Some
   Special Matrices, Linear Algebra Appl. 596, 203-215, 2020."""
    if nargout > 2:
        raise ValueError('Too many output arguments')
    if n == 0:
        return [], [], properties

    A = np.zeros((n, n), dtype=object)

    for i in range(1,n+1):
        for j in range(i, n+1):
            t = 1
            for k in range(2, i+1):
                t = t * (j + i - k) / (k - 1)
            A[i-1, j-1] = t * (j + i - 1)
            A[j-1, i-1] = A[i-1, j-1]

    R = np.zeros((n, n), dtype=float)
    for i in range(1,n):
        for j in range(i, n+1):
            R[i-1, j-1] = comb(j-1, i-1) * sqrt(i - 1)

    if nargout == 1:
        return A
    else:
        return A, R
