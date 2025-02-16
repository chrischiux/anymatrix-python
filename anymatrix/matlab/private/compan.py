import rogues.matrices.compan as rogues_compan
import numpy as np

def compan(u):

    if type(u) != np.ndarray:
        return np.array([])
    
    return rogues_compan(u)
 
# Copy docstring from original function
compan.__doc__ = rogues_compan.__doc__