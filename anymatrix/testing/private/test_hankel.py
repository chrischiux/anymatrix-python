import numpy as np
from matlab.private.hankel import hankel

def test_hankel(M):
    """Returns true if the given matrix M is equal to its Hankel matrix"""
    if M.ndim != 2 or M.shape[0] != M.shape[1]:
        return False
    
    h_matrix = hankel(M[:, 0], M[-1, :])
    
    if type(M) is int or type(M) is float:
        M =  np.array([[M]])
    
    return np.array_equal(M, h_matrix)
