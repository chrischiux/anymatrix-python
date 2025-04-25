import pytest
from collections import Counter
import numpy as np
from numpy.ma.testutils import assert_array_equal


# def test_list_sets(python_am, matlab_eng):
#     python_result = python_am.anymatrix("sets")
#     matlab_result = matlab_eng.anymatrix("sets")
#     assert Counter(python_result) == Counter(matlab_result)

def test_parser_single_matrix(python_am):
    result = python_am.matlab_format_parser('[1, 2; 3, 4]')
    expected = [np.array([[1., 2.], [3., 4.]])]
    assert_array_equal(result, expected)

def test_parser_multi_matrix(python_am):
    result = python_am.matlab_format_parser('[1, 2; 3, 4], [2, 2; 3, 4]')
    expected = [np.array([[1., 2.], [3., 4.]]), np.array([[2., 2.], [3., 4.]])]
    assert_array_equal(result, expected)

def test_parser_single_input(python_am):
    result = python_am.matlab_format_parser('1')
    expected = [1]
    assert_array_equal(result, expected)

def test_parser_multi_input(python_am):
    result = python_am.matlab_format_parser('1, 2')
    expected = [1, 2]
    assert_array_equal(result, expected)

def test_parser_mixed_input(python_am):
    result = python_am.matlab_format_parser('[1, 2; 3, 4], 12')
    expected = [np.array([[1., 2.], [3., 4.]]), 12]
    assert_array_equal(result[0], expected[0])
    assert result[1] == expected[1]
    assert isinstance(result, tuple)


def test_parser_mixed_input2(python_am):
    result = python_am.matlab_format_parser('12, [1, 2; 3, 4]')
    expected = [12, np.array([[1., 2.], [3., 4.]])]
    assert_array_equal(result[1], expected[1])
    assert result[0] == expected[0]
    assert isinstance(result, tuple)
