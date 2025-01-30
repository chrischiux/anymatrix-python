import rogues.matrices.compan as rogues_compan

def compan(u):
    """
    COMPAN  Companion matrix.
        compan(p) is a companion matrix.  There are three cases.
        If p is a scalar then compan(p) is the p-by-p matrix compan(1:p+1).
        If p is an (n+1)-vector, compan(p) is the n-by-n companion matrix
           whose first row is -p(2:n+1)/p(1).
        If p is a square matrix, compan(p) is the companion matrix
           of the characteristic polynomial of p, computed as
           compan(poly(p)).

        References:
        J.H. Wilkinson, The Algebraic Eigenvalue Problem,
           Oxford University Press, 1965, p. 12.
        G.H. Golub and C.F. Van Loan, Matrix Computations, second edition,
           Johns Hopkins University Press, Baltimore, Maryland, 1989,
           sec 7.4.6.
        C. Kenney and A.J. Laub, Controllability and stability radii for
          companion form systems, Math. Control Signals Systems, 1 (1988),
          pp. 239-256. (Gives explicit formulas for the singular values of
          COMPAN(P).)
    """
    
    return rogues_compan(u)

print(compan(3))