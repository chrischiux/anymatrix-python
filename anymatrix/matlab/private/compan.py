import numpy as np
""""
COMPAN  Complementary matrix.
A = COMPAN(U) returns the complementary matrix of the vector U.
Source code from: https://github.com/macd/rogues"""
def compan(u):

    if type(u) == int or type(u) == float:
        return np.array([])
    
    if type(u) != np.ndarray:
        u = np.array(u)
    
    n = np.size(u)
    if n <= 1:
        return np.array([])

    n = len(u)
    if n < 2:
        raise ValueError("Input vector must have at least two elements")
    
    A = np.zeros((n-1, n-1), dtype=float)
    if n > 1:
        A[0, :] = -u[1:] / u[0]
        A[1:, :-1] = np.eye(n-2)
    
    if A.shape == (1,1):
        return A[0,0]
    
    return A