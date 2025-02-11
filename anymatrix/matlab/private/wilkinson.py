import numpy as np

def wilkinson(n):

    m = (n-1)/2
    e = np.ones(n-1)
    W = np.diag(np.abs(np.arange(-m, m+1))) + np.diag(e, 1) + np.diag(e, -1)
    
    return W