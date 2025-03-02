import json, os, numpy
import numpy as np
import matlab.engine
from anymatrix import Anymatrix
np.set_printoptions(suppress=True)
am = Anymatrix()
python_data = am.anymatrix("matlab/pascal", 30)[28,29]
print(python_data)

# eng = matlab.engine.start_matlab()
# eng.cd(r"C:\Users\propo\OneDrive - University of Leeds\Documents\MATLAB\anymatrix", nargout=0)
# ans = eng.anymatrix("matlab/pascal", 30)
# converted = np.array(ans)
# matlab_data = converted[28,29]
# print(matlab_data)