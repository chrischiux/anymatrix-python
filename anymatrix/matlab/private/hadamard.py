import rogues.matrices.hadamard as rogues_hadamard

def hadamard(n):
    """
    HADAMARD  Hadamard matrix.
          HADAMARD(N) is a Hadamard matrix of order N, that is,
          a matrix H with elements 1 or -1 such that H*H' = N*EYE(N).
          An N-by-N Hadamard matrix with N>2 exists only if REM(N,4) = 0.
          This function handles only the cases where N, N/12 or N/20
          is a power of 2.

          Reference:
          S.W. Golomb and L.D. Baumert, The search for Hadamard matrices,
             Amer. Math. Monthly, 70 (1963) pp. 12-17.
          http://en.wikipedia.org/wiki/Hadamard_matrix
          Weisstein, Eric W. "Hadamard Matrix." From MathWorld--
             A Wolfram Web Resource:
             http://mathworld.wolfram.com/HadamardMatrix.html
    """
    
    return rogues_hadamard(n)

print(hadamard(4))