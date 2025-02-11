def test_matlab_toeplitz(am):
    A = am.anymatrix('matlab/toeplitz',[1, 1, 1], [1, 2, 2])
    anymatrix_check_props(am, A, 'matlab/toeplitz')

def test_matlab_hadamard(am):
    A = am.anymatrix('matlab/hadamard', 2)
    anymatrix_check_props(am, A, 'matlab/hadamard')
    A = am.anymatrix('matlab/hadamard', 4)
    anymatrix_check_props(am, A, 'matlab/hadamard')
    A = am.anymatrix('matlab/hadamard', 40)
    anymatrix_check_props(am, A, 'matlab/hadamard')