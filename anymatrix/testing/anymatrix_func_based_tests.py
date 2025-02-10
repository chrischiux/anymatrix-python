import pytest
from main import Anymatrix
from private import test_positive

@pytest.fixture
def am():
    am = Anymatrix()
    return am

def test_core_beta(am):
    A = am.anymatrix("core/beta", 3)
    if type(A) is tuple:
        A = A[0]
    assert test_positive.test_positive(A), "Not positive"
    
