import numpy as np

def invhilb(n, classname='double'):
   """INVHILB Inverse Hilbert matrix.
   IH = INVHILB(N) is the inverse of the N-by-N matrix with elements
   1/(i+j-1), which is a famous example of a badly conditioned matrix.
   The result is exact for N less than or equal to 12.

   IH = INVHILB(N,CLASSNAME) returns a matrix of class CLASSNAME, which
   can be either 'single' or 'double' (the default).

   Example:
  
   INVHILB(3) is
 
            9   -36    30
          -36   192  -180
           30  -180   180

   See also HILB.

   Copyright 1984-2018 The MathWorks, Inc.
   Description from MATLAB documentation."""
   if classname not in ['single', 'double']:
      raise ValueError("classname must be either 'single' or 'double'")
   
   dtype = np.float32 if classname == 'single' else np.float64
   
   H = np.zeros((n, n), dtype=dtype)
   p = n
   for i in range(1,n+1):
      r = p * p
      H[i-1, i-1] = r / (2 * i - 1)
      for j in range(i + 1, n+1):
         r = -((n - j+1) * r * (n + j - 1)) / ((j - 1) ** 2)
         # print(r)
         H[i-1, j-1] = r / (i + j - 1)
         H[j-1, i-1] = r / (i + j - 1)
      p = ((n - i) * p * (n + i)) / (i ** 2)
   
   return H