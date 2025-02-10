import rogues.matrices.hilb as rogues_hilb

def hilb(n, m=0):
    
    return rogues_hilb(n, m)

# Copy docstring from original function
hilb.__doc__ = rogues_hilb.__doc__