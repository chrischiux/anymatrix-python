import rogues.matrices.hankel as rogues_hankel

def hankel(a, b=None):
    
    return rogues_hankel(a,b)

# Copy docstring from original function
hankel.__doc__ = rogues_hankel.__doc__