import pytest
import sys
import os
from anymatrix import Anymatrix
import matlab.engine
from pathlib import Path

current = os.path.dirname(os.path.realpath(__file__))
parent = os.path.dirname(current)
sys.path.append(parent)

@pytest.fixture(scope="session")
def python_am():
    am = Anymatrix()
    return am

@pytest.fixture(scope="session")
def matlab_eng():
    eng = matlab.engine.start_matlab()
    # Insert path to Anymatrix-MATLAB installation
    current_file_path = str(Path(__file__).resolve().parent.parent)
    eng.cd(current_file_path + r"/anymatrix-matlab", nargout=0)
    return eng