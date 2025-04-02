import sys
import os

current = os.path.dirname(os.path.realpath(__file__))
parent = os.path.dirname(current)
sys.path.append(parent)

import pytest
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

def test_property_scan(python_am, matlab_eng):
    python_result = python_am.anymatrix("prop")
    matlab_result = matlab_eng.anymatrix("prop")
    assert Counter(python_result) == Counter(matlab_result)

# Each property alone
def test_property_search_alone(python_am, matlab_eng):
    properties = python_am.anymatrix("prop")
    for prop in properties:
        python_result = python_am.anymatrix("prop", prop)
        matlab_result = matlab_eng.anymatrix("prop", prop)
        assert Counter(python_result) == Counter(matlab_result), f"Property search mismatch: {prop}" 

# Eeach property alone negated
def test_property_search_negated(python_am, matlab_eng):
    properties = python_am.anymatrix("prop")
    for prop in properties:
        python_result = python_am.anymatrix("prop", "not " + prop)
        matlab_result = matlab_eng.anymatrix("prop", "not " + prop)
        assert Counter(python_result) == Counter(matlab_result), f"Property search mismatch: not {prop}"
        
# 2 property permutations union (or)
def test_property_search_union(python_am, matlab_eng):
    properties = python_am.anymatrix("prop")
    extended_properties = properties + [f"not {prop}" for prop in properties]
    permutations = itertools.product(extended_properties, repeat=2)
    for prop in permutations:
        python_result = python_am.anymatrix("prop", f"{prop[0]} or {prop[1]}")
        matlab_result = matlab_eng.anymatrix("prop", f"{prop[0]} or {prop[1]}")
        assert Counter(python_result) == Counter(matlab_result), f"Property search mismatch: {prop[0]} or {prop[1]}"
        
# 2 property permutations inersection (and)
def test_property_search_inersection(python_am, matlab_eng):
    properties = python_am.anymatrix("prop")
    extended_properties = properties + [f"not {prop}" for prop in properties]
    permutations = itertools.product(extended_properties, repeat=2)
    for prop in permutations:
        python_result = python_am.anymatrix("prop", f"{prop[0]} and {prop[1]}")
        matlab_result = matlab_eng.anymatrix("prop", f"{prop[0]} and {prop[1]}")
        assert Counter(python_result) == Counter(matlab_result), f"Property search mismatch: {prop[0]} or {prop[1]}"
        
# 3 property permutations with all combinations of "and" and "or"
# @pytest.mark.parametrize("prop", ["and", "or"])
# def test_property_search_three_term(python_am, matlab_eng, prop):
#     properties = python_am.anymatrix("prop")
#     extended_properties = properties + [f"not {prop}" for prop in properties]
#     permutations = itertools.product(extended_properties, repeat=3)
#     operators = ["and", "or"]
    
#     for prop in permutations:
#         for op1 in operators:
#             for op2 in operators:
#                 expression = f"{prop[0]} {op1} {prop[1]} {op2} {prop[2]}"
#                 python_result = python_am.anymatrix("prop", expression)
#                 matlab_result = matlab_eng.anymatrix("prop", expression)
#                 assert Counter(python_result) == Counter(matlab_result), f"Property search mismatch: {expression}"

# Generate permutations for parameterized test
properties = Anymatrix().anymatrix("prop")
extended_properties = properties + [f"not {prop}" for prop in properties]
permutations = list(itertools.permutations(extended_properties, 3))
operators = ["and", "or"]

@pytest.mark.parametrize("prop", permutations)
@pytest.mark.parametrize("op1", operators)
@pytest.mark.parametrize("op2", operators)
def test_property_search_three_term(python_am, matlab_eng, prop, op1, op2):
    expression = f"{prop[0]} {op1} {prop[1]} {op2} {prop[2]}"
    python_result = python_am.anymatrix("prop", expression)
    matlab_result = matlab_eng.anymatrix("prop", expression)
    assert Counter(python_result) == Counter(matlab_result), f"Property search mismatch: {expression}"