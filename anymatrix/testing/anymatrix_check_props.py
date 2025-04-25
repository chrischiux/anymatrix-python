import importlib.util, os
import numpy as np

def anymatrix_check_props(am, M, matrix_ID, supported_properties):
    # Get properties of matrix_ID
    properties = am.show_matrix_properties(matrix_ID)

    if type(M) == np.ndarray and M.dtype == object:
        M = M.astype(np.float64)

    # test for assertion for each suported property
    for prop in properties:
        if prop in supported_properties:
            # dynamic import test function
            handle_name = f"test_{prop}"
            spec = importlib.util.spec_from_file_location(handle_name, os.path.join(am.root_path, f"testing/private/test_{prop}.py"))
            module = importlib.util.module_from_spec(spec)
            spec.loader.exec_module(module)
            function = getattr(module, f"test_{prop}")
            # test property
            assert function(M), f"Property {prop} failed for matrix {matrix_ID}"