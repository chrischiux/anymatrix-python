import pytest
import matlab
import numpy as np

def test_matlab_rosser(python_am, matlab_eng):
    python_result = python_am.anymatrix("matlab/rosser")
    matlab_result = matlab_eng.anymatrix("matlab/rosser")
    converted = np.array(matlab_result)

    assert np.array_equal(converted, python_result), f"missmatch: matlab/rosser"


@pytest.mark.parametrize("arg", [10, 100, 1000])
def test_matlab_wilkinson(python_am, matlab_eng, arg):
    python_result = python_am.anymatrix("matlab/wilkinson", arg)
    matlab_result = matlab_eng.anymatrix("matlab/wilkinson", float(arg))
    converted = np.array(matlab_result)
    
    assert np.array_equal(converted, python_result), f"missmatch: matlab/wilkinson - {arg}"


@pytest.mark.parametrize("arg", [10, 100, 1000])
def test_matlab_spiral(python_am, matlab_eng, arg):
    python_result = python_am.anymatrix("matlab/spiral", arg)
    matlab_result = matlab_eng.anymatrix("matlab/spiral", float(arg))
    converted = np.array(matlab_result)
    
    assert np.array_equal(converted, python_result), f"missmatch: matlab/spiral - {arg}"


@pytest.mark.parametrize("arg", [10, 100, 1000])
def test_matlab_magic(python_am, matlab_eng, arg):
    python_result = python_am.anymatrix("matlab/magic", arg)
    matlab_result = matlab_eng.anymatrix("matlab/magic", float(arg))
    converted = np.array(matlab_result)

    assert np.array_equal(converted, python_result), f"missmatch: matlab/magic - {arg}"


@pytest.mark.parametrize("arg", [10, 100, 1000])
def test_matlab_invhilb(python_am, matlab_eng, arg):
    python_result = python_am.anymatrix("matlab/invhilb", arg)
    matlab_result = matlab_eng.anymatrix("matlab/invhilb", float(arg))
    converted = np.array(matlab_result)

    assert np.array_equal(converted, python_result), f"missmatch: matlab/invhilb - {arg}"


@pytest.mark.parametrize("arg", [10, 100, 1000])
def test_matlab_hilb(python_am, matlab_eng, arg):
    python_result = python_am.anymatrix("matlab/hilb", arg)
    matlab_result = matlab_eng.anymatrix("matlab/hilb", float(arg))
    converted = np.array(matlab_result)

    assert np.array_equal(converted, python_result), f"missmatch: matlab/hilb - {arg}"

@pytest.mark.parametrize("arg", [10, 100, 1000])
def test_matlab_hadamard(python_am, matlab_eng, arg):
    python_result = python_am.anymatrix("matlab/hadamard", arg)
    matlab_result = matlab_eng.anymatrix("matlab/hadamard", float(arg))
    converted = np.array(matlab_result)

    assert np.array_equal(converted, python_result), f"missmatch: matlab/hadamard - {arg}"


@pytest.mark.parametrize("arg", [10, 100, 1000])
def test_matlab_pascal(python_am, matlab_eng, arg):
    python_result = python_am.anymatrix("matlab/pascal", arg)
    matlab_result = matlab_eng.anymatrix("matlab/pascal", float(arg))
    converted = np.array(matlab_result)

    assert np.allclose(converted, python_result), f"missmatch: matlab/pascal - {arg}"


@pytest.mark.parametrize("arg", [10, 100, 1000])
def test_core_beta(python_am, matlab_eng, arg):
    python_result = python_am.anymatrix("core/beta", arg)
    matlab_result = matlab_eng.anymatrix("core/beta", float(arg))
    converted = np.array(matlab_result)

    assert np.array_equal(converted, python_result), f"missmatch: core/beta - {arg}"

# array input setup
input_arg = []
for i in [8, 128, 256, 512, 1024]:
    input_arg.append(list(range(1, i+1)))


@pytest.mark.parametrize("arg", input_arg)
def test_matlab_compan(python_am, matlab_eng, arg):
    python_result = python_am.anymatrix("matlab/compan", arg)
    matlab_result = matlab_eng.anymatrix("matlab/compan", matlab.double(arg))
    converted = np.array(matlab_result)

    assert np.array_equal(converted, python_result), f"missmatch: matlab/compan - {len(arg)}"


@pytest.mark.parametrize("arg", input_arg)
def test_matlab_vander(python_am, matlab_eng, arg):
    python_result = python_am.anymatrix("matlab/vander", arg)
    matlab_result = matlab_eng.anymatrix("matlab/vander", matlab.double(arg))
    converted = np.array(matlab_result)

    assert np.array_equal(converted, python_result), f"missmatch: matlab/vander - {len(arg)}"


@pytest.mark.parametrize("arg", input_arg)
def test_matlab_toeplitz(python_am, matlab_eng, arg):
    python_result = python_am.anymatrix("matlab/toeplitz", arg)
    matlab_result = matlab_eng.anymatrix("matlab/toeplitz", matlab.double(arg))
    converted = np.array(matlab_result)

    assert np.array_equal(converted, python_result), f"missmatch: matlab/toeplitz - {len(arg)}"

double_input_arg = []
for i in [10,100,1000]:
    double_input_arg.append([list(range(1, 1 + i)), list(range(i + 1, 1, -1))])
@pytest.mark.parametrize("arg", double_input_arg)
def test_matlab_toeplitz_tow_argument(python_am, matlab_eng, arg):
    python_result = python_am.anymatrix("matlab/toeplitz", arg[0], arg[1])
    matlab_result = matlab_eng.anymatrix("matlab/toeplitz", matlab.double(arg[0]), matlab.double(arg[1]))
    converted = np.array(matlab_result)

    assert np.array_equal(converted, python_result), f"missmatch: matlab/toeplitz (2 argument) - {len(arg[0])}"


@pytest.mark.parametrize("arg", input_arg)
def test_matlab_hankel(python_am, matlab_eng, arg):
    python_result = python_am.anymatrix("matlab/hankel", arg)
    matlab_result = matlab_eng.anymatrix("matlab/hankel", matlab.double(arg))
    converted = np.array(matlab_result)

    assert np.array_equal(converted, python_result), f"missmatch: matlab/hankel - {len(arg)}"

@pytest.mark.parametrize("arg", double_input_arg)
def test_matlab_hankel_two_argument(python_am, matlab_eng, arg):
    python_result = python_am.anymatrix("matlab/hankel", arg[0], arg[1])
    matlab_result = matlab_eng.anymatrix("matlab/hankel", matlab.double(arg[0]), matlab.double(arg[1]))
    converted = np.array(matlab_result)

    assert np.array_equal(converted, python_result), f"missmatch: matlab/hankel - {len(arg[0])}"