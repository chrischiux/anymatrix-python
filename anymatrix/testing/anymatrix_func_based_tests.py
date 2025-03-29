import sys, os
current = os.path.dirname(os.path.realpath(__file__))
parent = os.path.dirname(current)
sys.path.append(parent)
import pytest
from anymatrix import Anymatrix
from anymatrix_check_props import anymatrix_check_props

@pytest.fixture
def am():
    am = Anymatrix()
    return am

supported_properties = ['bidiagonal', 'binary', 'complex', 'hankel', 'hermitian', 'hessenberg', 'integer', 'nonnegative', 'permutation', 'positive', 'square', 'stochastic', 'symmetric', 'toeplitz', 'triangular', 'tridiagonal']

@pytest.mark.parametrize("args", [3, 5, 8, 10, 15, 24, 25, 30, 31])
def test_core_beta(am, args):
    A = am.anymatrix("core/beta", args)
    if type(A) is tuple:
        A = A[0]
    anymatrix_check_props(am, A, "core/beta", supported_properties)

@pytest.mark.parametrize("args", [3, 5, 8, 10, 15, 24, 25, 30, 31])
def test_matlab_compan(am, args):
    A = am.anymatrix("matlab/compan", args)
    if type(A) is tuple:
        A = A[0]
    anymatrix_check_props(am, A, "matlab/compan", supported_properties)

def test_matlab_hadamard(am):
    A = am.anymatrix('matlab/hadamard', 2)
    anymatrix_check_props(am, A, 'matlab/hadamard', supported_properties)
    A = am.anymatrix('matlab/hadamard', 4)
    anymatrix_check_props(am, A, 'matlab/hadamard', supported_properties)
    A = am.anymatrix('matlab/hadamard', 40)

@pytest.mark.parametrize("args", [3, 5, 8, 10, 15, 24, 25, 30, 31])
def test_matlab_hankel(am, args):
    A = am.anymatrix("matlab/hankel", args)
    if type(A) is tuple:
        A = A[0]
    anymatrix_check_props(am, A, "matlab/hankel", supported_properties)

@pytest.mark.parametrize("args", [3, 5, 8, 10, 15, 24, 25, 30, 31])
def test_matlab_hilb(am, args):
    A = am.anymatrix("matlab/hilb", args)
    if type(A) is tuple:
        A = A[0]
    anymatrix_check_props(am, A, "matlab/hilb", supported_properties)

@pytest.mark.parametrize("args", [3, 5, 8, 10, 15, 24, 25, 30, 31])
def test_matlab_invhilb(am, args):
    A = am.anymatrix("matlab/invhilb", args)
    if type(A) is tuple:
        A = A[0]
    anymatrix_check_props(am, A, "matlab/invhilb", supported_properties)

@pytest.mark.parametrize("args", [3, 5, 8, 10, 15, 24, 25, 30, 31])
def test_matlab_magic(am, args):
    A = am.anymatrix("matlab/magic", args)
    if type(A) is tuple:
        A = A[0]
    anymatrix_check_props(am, A, "matlab/magic", supported_properties)

@pytest.mark.parametrize("args", [3, 5, 8, 10, 15, 24, 25, 30, 31])
def test_matlab_pascal(am, args):
    A = am.anymatrix("matlab/pascal", args)
    if type(A) is tuple:
        A = A[0]
    anymatrix_check_props(am, A, "matlab/pascal", supported_properties)
def test_matlab_rosser(am):
    A = am.anymatrix("matlab/rosser")
    if type(A) is tuple:
        A = A[0]
    anymatrix_check_props(am, A, "matlab/rosser", supported_properties)

@pytest.mark.parametrize("args", [3, 5, 8, 10, 15, 24, 25, 30, 31])
def test_matlab_spiral(am, args):
    A = am.anymatrix("matlab/spiral", args)
    if type(A) is tuple:
        A = A[0]
    anymatrix_check_props(am, A, "matlab/spiral", supported_properties)

def test_matlab_toeplitz(am):
    A = am.anymatrix('matlab/toeplitz',[1, 1, 1], [1, 2, 2])
    anymatrix_check_props(am, A, 'matlab/toeplitz', supported_properties)

@pytest.mark.parametrize("args", [3, 5, 8, 10, 15, 24, 25, 30, 31])
def test_matlab_vander(am, args):
    A = am.anymatrix("matlab/vander", args)
    if type(A) is tuple:
        A = A[0]
    anymatrix_check_props(am, A, "matlab/vander", supported_properties)

@pytest.mark.parametrize("args", [3, 5, 8, 10, 15, 24, 25, 30, 31])
def test_matlab_wilkinson(am, args):
    A = am.anymatrix("matlab/wilkinson", args)
    if type(A) is tuple:
        A = A[0]
    anymatrix_check_props(am, A, "matlab/wilkinson", supported_properties)
