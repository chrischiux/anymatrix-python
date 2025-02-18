import rogues.matrices.hilb as rogues_hilb

def hilb(n):
    
    return rogues_hilb(n, 0)

# Copy docstring from original function
hilb.__doc__ = rogues_hilb.__doc__