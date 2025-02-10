import numpy as np

def test_complex(M):
    """Returns true if the given matrix M contains any complex numbers"""
    return np.iscomplexobj(M)