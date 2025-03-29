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

def test_supported_properties(python_am, matlab_eng):
    python_result = python_am.anymatrix("properties")
    matlab_result = matlab_eng.anymatrix("properties")
    assert Counter(python_result) == Counter(matlab_result)
    
def test_list_group(python_am, matlab_eng):
    python_result = python_am.anymatrix("group")
    matlab_result = matlab_eng.anymatrix("group")
    assert Counter(python_result) == Counter(matlab_result)


def test_list_group_matrix(python_am, matlab_eng):
    groups = python_am.anymatrix("group")
    for group in groups:
        python_result = python_am.anymatrix("groups", group)
        matlab_result = matlab_eng.anymatrix("groups", group)
        assert Counter(python_result) == Counter(matlab_result), f"Group member mismatch: {group}"

def test_list_matrix(python_am, matlab_eng):
    python_result = python_am.anymatrix("all")
    matlab_result = matlab_eng.anymatrix("all")
    assert Counter(python_result) == Counter(matlab_result)


def test_show_matrix_property(python_am, matlab_eng):
    matrices = python_am.anymatrix("all")
    for matrix in matrices:
        python_result = python_am.anymatrix("properties", matrix)
        matlab_result = matlab_eng.anymatrix("properties", matrix)
        assert Counter(python_result) == Counter(matlab_result), f"Property set mismatch: {matrix}"

