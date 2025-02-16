import rogues.utils.toeplitz as rogues_toeplitz
import numpy
def toeplitz(a, b=None):

    if type(a) is not numpy.ndarray:
        a = numpy.array(a)
    if b is not None and type(b) is not numpy.ndarray:
        b = numpy.array(b)
    return rogues_toeplitz(a, b)

# Copy docstring from original function
toeplitz.__doc__ = rogues_toeplitz.__doc__