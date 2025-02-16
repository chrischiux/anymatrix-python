import rogues.matrices.pascal as rogues_pascal

def pascal(n, k=0):

    return rogues_pascal(n, k)

# Copy docstring from original function
pascal.__doc__ = rogues_pascal.__doc__