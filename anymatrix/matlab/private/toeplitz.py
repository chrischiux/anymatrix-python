import rogues.utils.toeplitz as rogues_toeplitz
def toeplitz(a, b=None):

  return rogues_toeplitz(a, b)

# Copy docstring from original function
toeplitz.__doc__ = rogues_toeplitz.__doc__