import pytest
import sys
import os

current = os.path.dirname(os.path.realpath(__file__))
parent = os.path.dirname(current)
sys.path.append(parent)


from anymatrix import Anymatrix
import matlab.engine
import itertools
import numpy as np
from collections import Counter

@pytest.fixture(scope="module")
def python_am():
    am = Anymatrix()
    return am

@pytest.fixture(scope="module")
def matlab_eng():
    eng = matlab.engine.start_matlab()
    eng.cd(r"C:\Users\propo\OneDrive - University of Leeds\Documents\MATLAB\anymatrix", nargout=0)
    return eng

def test_list_sets(python_am, matlab_eng):
    python_result = python_am.anymatrix("sets")
    matlab_result = matlab_eng.anymatrix("sets")
    assert Counter(python_result) == Counter(matlab_result)