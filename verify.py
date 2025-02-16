import json, os, numpy
current_file_path = os.path.dirname(os.path.abspath(__file__))

# Define the path to the JSON file
json_file_path = current_file_path + '/python_test_set.json'

# Read the JSON file
with open(json_file_path, 'r') as file:
    python_data = json.load(file)

json_file_path = current_file_path + '/matlab_test_set.json'

# Read the JSON file
with open(json_file_path, 'r') as file:
    matlab_data = json.load(file)

success_count = 0
fail_count = 0

for i in range(len(python_data)-1):
    python_matrix = python_data[i]['matrix']
    matlab_matrix = matlab_data[i]['matrix']

    # compare the two matrices WITH tolerance
    if numpy.allclose(python_matrix,matlab_matrix):
        success_count += 1
        continue
    
    # try putting matlab result in 1x1 2d matrix and compare
    if numpy.allclose(python_matrix, [[matlab_matrix]]):
        success_count += 1
        continue
    
    print(f"{python_data[i]['matrix_ID']} {python_data[i]['parameters']} is not equal")
    fail_count += 1
        

print(f"Success: {success_count}")
print(f"Fail: {fail_count}")