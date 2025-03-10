import numpy as np
import rogues.matrices.pascal as rogues_pascal

def pascal(*args, **kwargs):
    """
    PASCAL  Pascal matrix.
        p = pascal(n) is the pascal matrix of order n: a symmetric positive
        definite matrix with integer entries taken from Pascal's
        triangle.
        The Pascal matrix is totally positive and its inverse has
        integer entries.  Its eigenvalues occur in reciprocal pairs.
        cond(p) is approximately 16**n/(n*pi) for large n.
        pascal(n,1) is the lower triangular cholesky factor (up to signs
        of columns) of the pascal matrix.   It is involutary (is its own
        inverse).
        pascal(n,2) is a transposed and permuted version of pascal(n,1)
        which is a cube root of the identity.
        specify classname as 'single' or 'double' to return a matrix of that class

        References:
        R. Brawer and M. Pirovino, The linear algebra of the Pascal matrix,
           Linear Algebra and Appl., 174 (1992), pp. 13-23 (this paper
           gives a factorization of L = PASCAL(N,1) and a formula for the
           elements of L^k).
        N.J. Higham, Accuracy and Stability of Numerical Algorithms,
           Society for Industrial and Applied Mathematics, Philadelphia, PA,
           USA, 2002; sec. 28.4.
        S. Karlin, Total Positivity, Volume 1, Stanford University Press,
           1968.  (Page 137: shows i+j-1 choose j is TP (i,j=0,1,...).
                   PASCAL(N) is a submatrix of this matrix.)
        M. Newman and J. Todd, The evaluation of matrix inversion programs,
           J. Soc. Indust. Appl. Math., 6(4):466--476, 1958.
        H. Rutishauser, On test matrices, Programmation en Mathematiques
           Numeriques, Editions Centre Nat. Recherche Sci., Paris, 165,
           1966, pp. 349-365.  (Gives an integral formula for the
           elements of PASCAL(N).)
        J. Todd, Basic Numerical Mathematics, Vol. 2: Numerical Algebra,
           Birkhauser, Basel, and Academic Press, New York, 1977, p. 172.
        H.W. Turnbull, The Theory of Determinants, Matrices, and Invariants,
           Blackie, London and Glasgow, 1929.  (PASCAL(N,2) on page 332.)

    Note added in porting: for pascal(10) the properties above seem to be
    verified, especially the eigenvalues being reprocal pairs (all of which
    have the same constant value of one).  det(pascal(n)) is also ~one up to
    and including n=17.  At n=18 things go to hell and this appears to be
    where we step off a cliff
    
    Fork of rogues module pascal function
    https://github.com/macd/rogues
    """
    # check number of argument
    nargin = len(args)
    if nargin == 0:
        raise ValueError("invalid input arguments")
    elif nargin == 1:
        n = args[0]
        k = 0
        classname = 'double'
    elif nargin == 2:
        n = args[0]
        if type(args[1]) is str:
            classname = args[1]
            k = 0
        elif type(args[1]) is int:
            k = args[1]
            classname = 'double'
        else:
            raise ValueError("second argument must be either an integer or a string")
    elif nargin == 3:
        n = args[0]
        k = args[1]
        classname = args[2]
    
    if classname not in ['single', 'double']:
        raise ValueError("classname must be either 'single' or 'double'")
    elif classname == 'single':
        classname = np.float32
    else:
        classname = np.float64
    
    # Matrix generation
    p = np.diag((-1) ** np.arange(n, dtype=classname))
    p[:, 0] = np.ones(n, dtype=classname)

    #  Generate the Pascal Cholesky factor (up to signs).
    for j in range(1, n - 1):
        for i in range(j + 1, n):
            p[i, j] = p[i - 1, j] - p[i - 1, j - 1]


    if k == 0:
        p = p @ p.T

    elif k == 2:
        p = np.rot90(p, 3)
        # CHECKME need to check .m file to see if this logic is correct
        if n / 2 == round(n / 2):
            p = -p

    return p