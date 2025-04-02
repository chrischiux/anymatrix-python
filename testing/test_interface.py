import pytest
from collections import Counter


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

