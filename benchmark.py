import itertools
import matlab.engine
import timeit
import statistics
from anymatrix import Anymatrix
from matplotlib.colors import Normalize
from matplotlib.cm import get_cmap
from matplotlib.table import Table
import matplotlib.pyplot as plt

am = Anymatrix()
eng = matlab.engine.start_matlab()
eng.cd(r"C:\Users\propo\OneDrive - University of Leeds\Documents\MATLAB\anymatrix", nargout=1)
eng.anymatrix(nargout=0)
am.anymatrix()

matrix_ID = ["matlab/wilkinson", "matlab/spiral", "matlab/magic", "matlab/invhilb", "matlab/hilb", "matlab/hadamard",
             "matlab/pascal", "core/beta"]
matrix_arg = [8, 128, 512]
# matrix_arg = [10, 100, 1000]
matrix_size = []

matlab_runtime = []
python_runtime = []

for matrix in matrix_ID:
    print(matrix)
    python_temp = []
    matlab_temp = []
    size_temp = []
    for arg in matrix_arg:
        print(arg)
        # Get MATLAB time
        matlab_func = f"@() anymatrix('{matrix}', {arg})"
        matlab_time = eng.eval(f"timeit({matlab_func})", nargout=1)
        matlab_temp.append(matlab_time)

        # Get python time
        timer = timeit.Timer(f"am.anymatrix('{matrix}', {arg})", globals=globals())
        loops, _ = timer.autorange()
        times = timer.repeat(1, loops)
        python_temp.append(statistics.median(times))

        # get matrix size
        matirx_size_temp = eng.eval(f"anymatrix('{matrix}', {arg})", nargout=1)
        size_temp.append(matirx_size_temp.size)

    matlab_runtime.append(matlab_temp)
    python_runtime.append(python_temp)

matrix_ID = ["matlab/compan", "matlab/hankel", "matlab/vander", "matlab/toeplitz"]
matrix_arg = []
for i in [8, 128, 512]:
    matrix_arg.append(list(range(1, 1 + i)))


for matrix in matrix_ID:
    print(matrix)
    python_temp = []
    matlab_temp = []
    size_temp = []
    for arg in matrix_arg:
        print(arg)
        # Get MATLAB time
        matlab_func = f"@() anymatrix('{matrix}', {arg})"
        matlab_time = eng.eval(f"timeit({matlab_func})", nargout=1)
        matlab_temp.append(matlab_time)

        # Get python time
        timer = timeit.Timer(f"am.anymatrix('{matrix}', {arg})", globals=globals())
        loops, total_time = timer.autorange()
        python_temp.append(total_time/loops)

        # get matrix size
        matirx_size_temp = eng.eval(f"anymatrix('{matrix}', {arg})", nargout=1)
        size_temp.append(matirx_size_temp.size)

    matlab_runtime.append(matlab_temp)
    python_runtime.append(python_temp)

# Create figure and axis
fig, ax = plt.subplots(figsize=(8, 6))
ax.axis('off')

# Create table
matrix_ID = ["matlab/wilkinson", "matlab/spiral", "matlab/magic", "matlab/invhilb", "matlab/hilb", "matlab/hadamard",
             "matlab/pascal", "core/beta", "matlab/compan", "matlab/hankel", "matlab/vander", "matlab/toeplitz"]
table_data = []
values = []
for i in range(len(matrix_ID)):
    row = [matrix_ID[i]]
    for j in range(len(matrix_arg)):
        value = python_runtime[i][j] / matlab_runtime[i][j]
        row.append(f"{value:.2f}")
        values.append(value)
    table_data.append(row)

# Add header
matrix_arg = [8,128,512]
header = ['Matrix'] + matrix_arg
table_data.insert(0, header)

# Normalize values for colormap
norm = Normalize(vmin=min(values), vmax=max(values))
cmap = get_cmap('autumn_r')  # Reverse the colormap by adding '_r'

# Create table
table = Table(ax, bbox=[0, 0, 1, 1])
n_rows, n_cols = len(table_data), len(table_data[0])

# Add cells
for i in range(n_rows):
    for j in range(n_cols):
        cell_text = table_data[i][j]
        if i == 0 or j == 0:
            # Header cells
            table.add_cell(i, j, width=1/n_cols, height=1/n_rows, text=cell_text, loc='center', facecolor='lightgrey')
        else:
            # Data cells
            value = float(cell_text)
            color = cmap(norm(value))
            table.add_cell(i, j, width=1/n_cols, height=1/n_rows, text=cell_text, loc='center', facecolor=color)

# Add table to axis
ax.add_table(table)

# Display plot
plt.show()