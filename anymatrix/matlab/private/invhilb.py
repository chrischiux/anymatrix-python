import rogues.matrices.hilb as rogues_hilb
from numpy.linalg import inv

def invhilb(n, m=0):
    """
    invhilb   inverse of Hilbert matrix.
       For description of the Hilbert matrix, see hilb.
    """
    
    return inv(rogues_hilb(n, m))