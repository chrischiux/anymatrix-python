import numpy as np
def test_square(M):
    """Returns true if number of rows equals number of columns in the given matrix M"""
    if M.size == 0:
        return True
    if M.shape[0] == M.shape[1]:
        return True
    else:
        return False