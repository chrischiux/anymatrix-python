import pytest
from collections import Counter

def test_list_sets(python_am, matlab_eng):
    python_result = python_am.anymatrix("sets")
    matlab_result = matlab_eng.anymatrix("sets")
    assert Counter(python_result) == Counter(matlab_result)