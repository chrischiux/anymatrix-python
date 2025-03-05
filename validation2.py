import pytest
from anymatrix import Anymatrix
import matlab.engine
import itertools
import numpy as np

am = Anymatrix()
eng = matlab.engine.start_matlab()
eng.cd(r"C:\Users\propo\OneDrive - University of Leeds\Documents\MATLAB\anymatrix", nargout=1)


matrix_ID = ["matlab/wilkinson", "matlab/spiral",  "matlab/magic", "matlab/invhilb", "matlab/hilb", "matlab/hadamard", "core/beta"]
matrix_size = [8, 128, 1024, 8192]
comb = list(itertools.product(matrix_ID, matrix_size))
counter = 0
for args in comb:
    python_result = am.anymatrix(args[0], args[1])
    matlab_result = eng.anymatrix(args[0], float(args[1]))

    converted = np.array(matlab_result)
    
    result = np.array_equal(python_result, converted)
    if result == False:
        print(args, result)
    else:
        print(args, result)
        counter+=1

print(counter)