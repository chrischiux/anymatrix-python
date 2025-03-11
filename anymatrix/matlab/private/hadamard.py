import rogues.matrices.hadamard as rogues_hadamard
import numpy as np

def hadamard(n, classname='double'):
    
   matrix = rogues_hadamard(n)
   if classname == 'single':
     return matrix.astype(np.float32)
   elif classname == 'double':
      return matrix
   else:
      raise ValueError("classname must be 'single' or 'double'")

# Copy docstring from original function
hadamard.__doc__ = rogues_hadamard.__doc__