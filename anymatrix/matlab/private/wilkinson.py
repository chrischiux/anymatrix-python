import numpy as np

def wilkinson(n):
    """
    Wilkinson's eigenvalue test matrix
    Function logic from MATLAB function wilkinson()
    See: https://uk.mathworks.com/help/matlab/ref/wilkinson.html
    """
    m = (n-1)/2
    e = np.ones(n-1)
    W = np.diag(np.abs(np.arange(-m, m+1))) + np.diag(e, 1) + np.diag(e, -1)
    
    return W