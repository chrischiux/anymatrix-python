import rogues.matrices.wilkinson as rogues_wilkinson
def wilkinson(n):
    """
    wilkinson array of size n where n must be odd.
    This is what some others call a Wilkinson array for arbitrary n. Note
    that Higham only uses this definition for n = 21
    """
    return rogues_wilkinson(n)