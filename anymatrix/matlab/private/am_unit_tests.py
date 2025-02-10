def test_matlab_toeplitz(am):
    A = am.anymatrix('matlab/toeplitz',[1, 1, 1], [1, 2, 2])
    anymatrix_check_props(am, A, 'matlab/toeplitz')