import pytest
from anymatrix import Anymatrix
import matlab.engine
import itertools
import numpy as np

@pytest.fixture
def python_am():
    am = Anymatrix()

@pytest.fixture
def matlab_eng():
    eng = matlab.engine.start_matlab()
    eng.cd(r"C:\Users\propo\OneDrive - University of Leeds\Documents\MATLAB\anymatrix", nargout=0)
    return eng

matrix_ID = ["matlab/wilkinson", "matlab/spiral"]
matrix_size = [10]
comb = list(itertools.product(matrix_ID, matrix_size))

@pytest.mark.parametrize("args", comb)
def test_matrix_generator(python_am, matlab_eng, args):
    python_result = python_am.anymatrix(args[0], args[1])
    matlab_result = matlab_eng.anymatrix(args[0], args[1])
    converted = np.array(matlab_result)
    assert(np.array_equal(python_result, converted))
