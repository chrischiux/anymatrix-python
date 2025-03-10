import numpy as np

def wilkinson(n, classname='double'):
    """
    Wilkinson's eigenvalue test matrix
    Function logic from MATLAB function wilkinson()
    See: https://uk.mathworks.com/help/matlab/ref/wilkinson.html
    """
    if classname == 'double':
        classname = np.float64
    elif classname == 'single':
        classname = np.float32
    else:
        raise ValueError('Invalid classname. Use "double" or "single".')
    
    m = (n-1)/2
    e = np.ones(n-1, dtype=classname)
    W = np.diag(np.abs(np.arange(-m, m+1, dtype=classname))) + np.diag(e, 1) + np.diag(e, -1)
    
    return W