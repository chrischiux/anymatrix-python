import rogues.utils.toeplitz as rogues_toeplitz
import numpy
def toeplitz(a, b=None):
    """
    toeplitz(a) returns a toeplitz matrix given "a", the first row of the
    matrix.  This matrix is defined as:

        [ [   a[0], a[1], a[2], a[3], ...,   a[n] ],
          [   a[n], a[0], a[1], a[2], ..., a[n-1] ],
          [ a[n-1], a[n], a[0], a[1], ..., a[n-2] ],
          ...
          [   a[1], a[2], a[3], a[4], ...,   a[0] ]]

    Note that this array is more properly called a "circulant" because each
    row is a circular shift of the one above it. Also, note that the main
    diagonal is constant and given by a[0].  If the array "a" is complex,
    the elements rotated to be under the main diagonal are complex conjugated
    to yield a Hermetian matrix.

    If called as toeplitz(a, b) then create the unsymetric toeplitz matrix.
    Here "b" would be the first row and "a" would be the first column. (This
    is bass-ackwards to follow the m*lab convention.) The second row shifts
    the first row to the right by one, but instead circularly shifting the
    last element of the row back into the first element, we shift in the
    successive elements of a as the element of b are shifted out.

    See the wikipedia entry for more information and references (especially the
    following: http://ee.stanford.edu/~gray/toeplitz.pdf)
    """
    if type(a) is not numpy.ndarray:
        a = numpy.array(a)
    if b is not None and type(b) is not numpy.ndarray:
        b = numpy.array(b)
    return rogues_toeplitz(a, b)