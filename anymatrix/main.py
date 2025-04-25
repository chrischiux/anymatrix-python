import os, re, pytest
import importlib.util
from . import prop_list
import json
import subprocess
import shutil


class Anymatrix:

    def __init__(self):
        self.root_path = os.path.dirname(os.path.abspath(__file__))
        self.built_in_groups = [
            'contest', 'core', 'gallery', 'hadamard', 
            'matlab', 'nessie', 'regtools'
        ]
        self.files_scanned = False
        self.set_IDs = []
        self.group_IDs = []
        self.matrix_IDs = []
        self.properties = []
        self.supported_properties = prop_list.prop_list()

        # self.scan_filesystem()


    def scan_filesystem(self):
        self.set_IDs = self.scan_sets()
        self.group_IDs = self.scan_groups()
        self.matrix_IDs = self.scan_matrices(self.group_IDs)
        self.properties = self.scan_properties(self.matrix_IDs)
    
    def scan_sets(self):
        """Scan the sets folder and obtain the set IDs."""

        sets_path = os.path.join(self.root_path, 'sets')
        IDs = [f for f in os.listdir(sets_path) if f.endswith('.txt')]

        # Remove '.txt' extensions from the IDs.
        IDs = [os.path.splitext(file)[0] for file in IDs]

        return IDs
    # Scan the group folders and obtain the matrix IDs.
    def scan_matrices(self, groups):
        matrix_IDs = []
        for group in groups:
            path_to_group = os.path.join(self.root_path, group, 'private')
            m_files = [f for f in os.listdir(path_to_group) if f.endswith('.py')]
            for m_file in m_files:
                with open(os.path.join(path_to_group, m_file), 'r') as file:
                    contents = file.read()
                    if 'properties = [' in contents:
                        matrix_IDs.append(f"{group}/{os.path.splitext(m_file)[0]}")
            
            # Read matrix IDs that are placed in properties.m files and
            # add them if they are not in yet from the M-files.
            am_properties_path = os.path.join(path_to_group, 'am_properties.py')
            if(os.path.isfile(am_properties_path)):
                spec = importlib.util.spec_from_file_location(f"anymatrix_{group}", am_properties_path)
                module = importlib.util.module_from_spec(spec)
                spec.loader.exec_module(module)
                for IDs in module.P:
                    moreIDs = f"{group}/{IDs[0]}"
                    if moreIDs not in matrix_IDs:
                        matrix_IDs.append(moreIDs)
        
        return matrix_IDs
    
    def search_by_properties(self, expression):
        IDs = []
        expression_array = expression.split()
        supported_properties_formated = [prop.replace(' ', '_') for prop in self.supported_properties]
        supported_properties_formated = [prop.replace('-', '_') for prop in supported_properties_formated]
        
        # Combine 2 word properties into one word.
        expression_length = len(expression_array)-1
        for i in range(expression_length):
            
            # break if we reach the end of the array
            if i >= expression_length:
                break
            
            if expression_array[i] not in ['and', 'or', 'not'] and expression_array[i+1] not in ['and', 'or', 'not']:
                expression_array[i] = expression_array[i] + "_" +expression_array[i+1]
                expression_array.pop(i+1)
                expression_length -= 1
                
        # update expression to include hyphens
        expression = ' '.join(expression_array)
    
        # evaluate the expression for each matrix
        for i, properties in enumerate(self.properties):
            new_expression = expression
            
            # Replace spaces with underscore in properties
            properties = [prop.replace(' ', '_') for prop in properties]
            properties = [prop.replace('-', '_') for prop in properties]
                
            # Create logical expression for evaluation
            
            for word in expression_array:
                if word in supported_properties_formated:
                    if word in properties:
                        new_expression = new_expression.replace(word, 'True', 1)
                    else:
                        new_expression = new_expression.replace(word, 'False', 1)
            try:
                if eval(new_expression):
                    IDs.append(self.matrix_IDs[i])
            except:
                pass
        return IDs
        

    # Scan the root folder and obtain the group IDs.
    def scan_groups(self):
        group_IDs = []
        contents = os.listdir(self.root_path)
        for items in contents:

            # Check if item is a directory.
            if os.path.isdir(f"{self.root_path}/{items}"):

                # Check if item is a group directory.
                if self.is_group_dir(items):
                    group_IDs.append(items)
        return group_IDs

    # Check if a folder in anymatrix root directory is a group folder.
    # Group directories have one private/ directory and one file named
    # anymatrix_<dir_name>.py where <dir_name> is the directory name.
    def is_group_dir(self, directory):
        dir_path = os.path.join(self.root_path, directory)
        # Check dir has two files
        if len(os.listdir(dir_path)) != 2:
            return False
        # Check if anymatrix_<dir_name>.py exists
        if not os.path.isfile(os.path.join(dir_path, f'anymatrix_{directory}.py')):
            return False
        # Check if private directory exists
        if not os.path.isdir(os.path.join(dir_path, 'private')):
            return False
        return True
    
    def lookfor_term(self, term):
        found_IDs = []
        for matrix_ID in self.matrix_IDs:
            group_name = matrix_ID.split('/')[0]
            matrix_name = matrix_ID.split('/')[1]
            handle_name = f'anymatrix_{group_name}_{matrix_name}'
            path_to_group = os.path.join(self.root_path, group_name, 'private')

            if os.path.isfile(os.path.join(path_to_group, f"{matrix_name}.py")):
                spec = importlib.util.spec_from_file_location(handle_name, os.path.join(path_to_group, f"{matrix_name}.py"))
                module = importlib.util.module_from_spec(spec)
                spec.loader.exec_module(module)
                if hasattr(module, matrix_name):
                    function = getattr(module, matrix_name)

                    # Check if docstring exist and term is in docstring of function
                    if function.__doc__ is not None and term in function.__doc__:
                        found_IDs.append(matrix_ID)
        return found_IDs

    def show_contents(self, group_ID):
        if os.path.isfile(f"{self.root_path}/{group_ID}/private/Contents.py"):
            self.type(f"{self.root_path}/{group_ID}/private/Contents.py")
        else:
            raise ValueError('No Contents.py exists for that group.')

    def show_matrix_help(self, matrix_ID):
        group_name = matrix_ID.split('/')[0]
        matrix_name = matrix_ID.split('/')[1]
        handle_name = f'anymatrix_{group_name}'
        path_to_group = os.path.join(self.root_path, group_name, 'private')
        if os.path.isfile(os.path.join(path_to_group, f"{matrix_name}.py")):
            spec = importlib.util.spec_from_file_location(handle_name, os.path.join(path_to_group, f"{matrix_name}.py"))
            module = importlib.util.module_from_spec(spec)
            spec.loader.exec_module(module)
            if hasattr(module, matrix_name):
                help(getattr(module, matrix_name))
            else:
                raise AttributeError(f"The module {matrix_name} not found.")

    def type(self, dir_path):
        # open file
        with open(dir_path, 'r') as file:
            # print file contents
            print(file.read())

    def generate_matrix(self, matrix_ID, varargin):
        group_name = matrix_ID.split('/')[0]
        matrix_name = matrix_ID.split('/')[1]
        handle_name = f'anymatrix_{group_name}'
        path_to_group = os.path.join(self.root_path, group_name, 'private')
        if os.path.isfile(os.path.join(path_to_group, f"{matrix_name}.py")):
            spec = importlib.util.spec_from_file_location(handle_name, os.path.join(path_to_group, f"{matrix_name}.py"))
            module = importlib.util.module_from_spec(spec)
            spec.loader.exec_module(module)
            if hasattr(module, matrix_name):
                generate_function = getattr(module, matrix_name)
                result = generate_function(*varargin)
                return result
            else:
                raise AttributeError(f"module {matrix_name} not found")
        else:
            raise FileNotFoundError(f"File {matrix_name}.py does not exist in path {path_to_group}.")

    def get_properties(self, matrix_ID):
        group_name = matrix_ID.split('/')[0]
        path_to_group = os.path.join(self.root_path, group_name, 'private')
        matrix_name = matrix_ID.split('/')[1]
        handle_name = f'anymatrix_{group_name}'
        P = []

        # Get properties from the Python file of the matrix.
        mfile_path = os.path.join(path_to_group, f'{matrix_name}.py')
        if os.path.isfile(mfile_path):
            with open(mfile_path, 'r') as file:
                mfile_contents = file.read()
                if 'properties =' in mfile_contents or 'properties=' in mfile_contents:
                    spec = importlib.util.spec_from_file_location(handle_name, mfile_path)
                    module = importlib.util.module_from_spec(spec)
                    spec.loader.exec_module(module)
                    P = module.properties
        # Get other properties from the entry in the properties.py file.
        am_properties_path = os.path.join(path_to_group, 'am_properties.py')
        if os.path.isfile(am_properties_path):
            spec = importlib.util.spec_from_file_location('am_properties', am_properties_path)
            module = importlib.util.module_from_spec(spec)
            spec.loader.exec_module(module)
            for prop in module.P:
                if matrix_name in prop:
                    temp = prop[1]
                    P.extend([prop for prop in temp if prop not in P])
        return P

    def scan_properties(self, matrix_IDs):
        P = []
        for matrix_ID in matrix_IDs:
            current_properties = self.get_properties(matrix_ID)
            P.append(current_properties)

        # Add property 'built-in' for the built-in matrices.
        for i, matrix_ID in enumerate(matrix_IDs):
            if any(matrix_ID.startswith(group) for group in self.built_in_groups):
            # if any(group.startswith(matrix_ID) for group in self.built_in_groups):
                P[i].append('built-in')

        # Add parent properties if not specified.
        M = {
        'banded': ['tridiagonal', 'bidiagonal'],
        'binary': ['permutation'],
        'integer': ['binary'],
        'nonnegative': ['binary', 'positive', 'stochastic', 'totally nonnegative'],
        'orthogonal': ['permutation'],
        'positive': ['totally positive'],
        'symmetric': ['correlation', 'hankel'],
        'positive definite': ['correlation'],
        'totally nonnegative': ['totally positive'],
        'triangular': ['bidiagonal']}

        I = {'real': ['complex'],
            'scalable': ['fixed size'],
            'square': ['rectangular']}
        
        for i in range(len(P)):
            for j in range(len(I)):
                # Find properties that can be added due to absence of some other properties.
                if not any(prop in P[i] for prop in I[list(I.keys())[j]]) and list(I.keys())[j] not in P[i]:
                    P[i].append(list(I.keys())[j])

            j = 0
            while j < len(M):
                # Find parent properties of any of the properties already in the list and add them if they are not in yet.
                if any(prop in P[i] for prop in M[list(M.keys())[j]]) and list(M.keys())[j] not in P[i]:
                    P[i].append(list(M.keys())[j])
                    j = 0
                j += 1

        # Check if all the properties can be recognized.
        for i in range(len(matrix_IDs)):
            for bad_prop in [prop for prop in P[i] if prop not in self.supported_properties]:
                if bad_prop:
                    print(f"Warning: Property {bad_prop} in {matrix_IDs[i]} is not recognized.")

        return P
    
    def show_matrix_properties(self, matrix_ID):
        for i in range(len(self.matrix_IDs)):
            if matrix_ID == self.matrix_IDs[i]:
                return self.properties[i]
            
    def matlab_format_parser(self, s):
        """Function to parse sets in MATLAB format and return the parameters as a tuple"""
        parameter = []
        i = 0
        while i < len(s):
            if s[i] == '[':
                # Find the closing bracket
                j = i
                while s[j] != ']':
                    j += 1
                # Extract the array string and convert to NumPy array
                array_str = s[i+1:j]
                # check if input is matrix or vector
                if ';' in array_str:
                    rows = array_str.split(';')
                    np_array = np.vstack([np.fromstring(row, sep=',') for row in rows])
                    parameter.append(np.array(np_array))
                else:
                    parameter.append(np.fromstring(array_str, sep=','))
                i = j + 1
            elif s[i].isdigit() or (s[i] == '-' and s[i+1].isdigit()):
                # Extract the integer
                j = i
                while j < len(s) and (s[j].isdigit() or s[j] == '-'):
                    j += 1
                parameter.append(int(s[i:j]))
                i = j
            else:
                i += 1
        return tuple(parameter)

    def update_git_group(self, group_ID, repo_ID):
        group_folder = self.root_path + '/' + group_ID + '/'
        # If the group does not exist locally, create folders and clone it.
        if not os.path.isdir(group_folder):
            if repo_ID.count('/') > 1 or ':' in repo_ID or '@' in repo_ID:
                repo_url = repo_ID
            else:
                repo_url = 'https://github.com/' + repo_ID + '.git'

            cmd = ['git', 'clone', repo_url, group_folder+'/private']

            status = subprocess.run(cmd, capture_output=True, text=True)

            if status.returncode == 0:
                print(f"Anymatrix remote group cloned.")
            else:
                # shutil.rmtree(group_folder)
                pass
        else: # Group exists. Run git pull to update it.
            if not os.path.isdir(group_folder + '/private/.git'):
                print("Specified group is not a git group.")
                return
            else:
                current_dir = os.getcwd()
                os.chdir(group_folder+'/private')
                result = subprocess.run(
                    ['git', 'pull'],
                    check=True,
                    text=True,
                    capture_output=True
                )
                os.chdir(current_dir)
                print(result.stdout.strip())

    def anymatrix(self, *varargin):
        """ANYMATRIX  Interface for accessing the Anymatrix collections.
    ANYMATRIX is a user interface for the Anymatrix matrix collection.
    It provides commands to list matrices, groups and sets, search for
    matrices by properties, and obtain the matrices by their IDs.

    The interface comes with built-in groups of matrices, but users can
    develop their own groups and make them available to other users.

    The built-in collection contains 7 groups:

    contest  - the CONTEST test matrix toolbox of random matrices
                from networks.
    core     - miscellaneous matrices.
    gallery  - matrices from the MATLAB gallery.
    hadamard - a large collection of (complex) Hadamard matrices.
    matlab   - other MATLAB matrices (not in gallery).
    nessie   - matrices from real-life networks.
    regtools - matrices from regularization problems.

    Anymatrix accepts the following commands. All arguments are character
    vectors or strings, except ones defined by the matrix M-files which
    might take various types of arguments.

    help anymatrix - display this information.
    ANYMATRIX('all') - return all matrix IDs in the collection.
    ANYMATRIX('contents', group_name) - displays Contents.m of the group
    with a specified name group_name.
    G = ANYMATRIX('groups') - return the available groups.
    M = ANYMATRIX('groups', group_name) - return matrix IDs that belong
    to the group with a specified name group_name.
    ANYMATRIX('groups', group_name, repository) - clone or update
    an anymatrix group stored in the specified repository.
    ANYMATRIX('help', matrix_id) - list the help for a specified
    matrix (anymatrix(matrix_id, 'help') also accepted).
    M = ANYMATRIX('lookfor', pattern) - returns a list of matrix IDs
    whose help comments contain the specified string/char pattern.
    ANYMATRIX('properties') - show the list of recognized properties.
    ANYMATRIX('properties', matrix_id) - list the properties of a
    specified matrix (anymatrix(matrix_id, 'properties') also
    accepted).
    M = ANYMATRIX('properties', properties) - list matrices having
    the specified properties.
    ANYMATRIX('scan') - force a scan of the file system.
    S = ANYMATRIX('sets') - return the available sets.
    [s, mat1, ..., matK] = ANYMATRIX('sets', set_name) - return matrix IDs
    in S and generate matrices in a specified set.
    ANYMATRIX('test') - run tests of all groups, where available.
    ANYMATRIX('test', group_name) - run tests of the specified group, if
    available.
    [out1, ..., outK] = ANYMATRIX(matrix_id, in1, ..., inN) - get the
    matrix with a specified matrix id and parameters (if any) in1 to
    inN. Some matrices supply multiple output arguments.

    Shorthand commands with one or more of the starting letters are also
    accepted, for example 'c', 'cont', 'g', 'gr', 'h', 'l', 'p', 'prop',
    'sc', 'se', 't'.

    Anymatrix supports logical queries to search for matrices by
    properties. In the command anymatrix('properties', '[properties]'), the
    list of properties is a single character vector containing properties
    that have to be separated by an "and" or an "or" and can be preceded by
    a "not". Brackets can also be included to specify precedence.

    Anymatrix holds the information about the underlying database of
    matrices in the persistent variables that are initialized by scanning
    the data on the first call to any command. To force an update to these
    variables use anymatrix('scan').

    Documentation:
    Nicholas J. Higham and Mantas Mikaitis, Anymatrix: An Extendable MATLAB
    Matrix Collection, User's Guide, MIMS EPrint 2021.15, Manchester
    Institute for Mathematical Sciences, The University of Manchester,
    UK, October 2021.

    References and acknowledgments.

    The CONTEST toolbox is included with permission from
    Alan Taylor and Desmond J. Higham.  CONTEST: A controllable test matrix
    toolbox for MATLAB. ACM Trans. Math. Software, 35(4):26:1-26:17, 2009.
    https://doi.org/10.1145/1462173.1462175

    The Hadamard group is reproduced with permission from
    N. J. A. Sloane, A Library of Hadamard Matrices,
    http://neilsloane.com/hadamard/. "Anything free comes with no guarantee".

    The NESSIE collection is included with permission from
    https://outreach.mathstat.strath.ac.uk/outreach/nessie/nessie_transport.html
    Alan Taylor and Desmond J. Higham, NESSIE: Network Example Source
    Supporting Innovative Experimentation, in Ernesto Estrada, Maria
    Fox, Desmond J. Higham and Gian-Luca Oppo, eds, Network Science:
    Complexity in Nature and Technology, pp. 85-106, Springer, 2010.
    https://doi.org/10.1007/978-1-84996-396-1_5

    The regtools group is included with permission from the
    Regulariation Tools toolbox at https://www.imm.dtu.dk/~pcha/Regutools/
    P. C. Hansen Regularization Tools: A Matlab package for analysis and
    solution of discrete ill-posed problems.  Numer. Algorithms 6(1), 1--35
    (1994).  https://doi.org/10.1007/BF02149761
    P. C. Hansen: Regularization Tools version 4.0 for Matlab 7.3.
    Numer. Algorithms 46(2), 189--194 (2007).
    https://doi.org/10.1007/s11075-007-9136-9"""
        # use matlab style variable names
        nargin = len(varargin)

        # Matrix ID pattern
        matrix_ID_pat = re.compile(r'[a-zA-Z0-9_-]+/[a-zA-Z0-9_-]+')

        if not self.files_scanned:
            self.scan_filesystem()
            self.files_scanned = True
            print("Automatic anymatrix scanning done.")

        if nargin == 0:
            help(Anymatrix.anymatrix)
            return
        
        # Parse the arguments passed to anymatrix.
        command = varargin[0]
        if nargin >= 2:
            arg = varargin[1]
            if type(varargin[1]) is str and any(varargin[1].startswith(valid_command) for valid_command in
                                                ['properties', 'groups', 'sets', 'all', 'scan', 'help', 'test',
                                                 'lookfor', 'contents']):
                command = varargin[1]
                arg = varargin[0]
            # Allow use of hyphens instead of underscores, but replace here.
            if type(arg) is str and not any(
                    command.startswith(valid_command) for valid_command in
                    ['lookfor', 'sets']):
                arg = arg.replace('-', '_')
        # Hyphens -> underscores in matrix IDs.
        command = command.replace('-', '_')

        # Capture some common errors in the arguments.
        if re.match(matrix_ID_pat, command):
            if command not in self.matrix_IDs:
                raise ValueError('Specified matrix ID was not found.')
        elif not any([x.startswith(command) for x in ['properties', 'groups', 'sets', 'all', 'scan', 'help', 'test', 'lookfor', 'contents']]):
            raise ValueError('Anymatrix command was not recognized.')
        elif nargin == 1:
            if any([x.startswith(command) for x in ['lookfor', 'contents']]):
                raise ValueError('Please specify one more argument.')
        elif nargin == 2:
            if type(arg) is not str:
                raise TypeError('This anymatrix command requires string arguments.')
            elif 'help'.startswith(command) or ('properties'.startswith(command) and re.match(matrix_ID_pat, arg)):
                if arg not in self.matrix_IDs:
                    raise ValueError('Specified matrix ID was not found.')
            elif any(prefix.startswith(command) for prefix in ['groups', 'contents', 'test']):
                if not arg in self.group_IDs:
                    raise ValueError('The specified group ID was not found.')

        # Execute the specified command.
        if 'all'.startswith(command):
            return self.matrix_IDs
        
        elif 'contents'.startswith(command):
            self.show_contents(arg)
        
        elif 'groups'.startswith(command):
            if nargin == 1:
                return self.group_IDs
            elif nargin == 2:
                return [matrix_id for matrix_id in self.matrix_IDs if matrix_id.startswith(f"{arg}/")]
            else:
                self.update_git_group(varargin[1], varargin[2])
                # print("Not implemented yet.")

        elif 'help'.startswith(command):
            if nargin == 1:
                help(Anymatrix.anymatrix)
            else:
                self.show_matrix_help(arg)
        
        elif 'lookfor'.startswith(command):
            return self.lookfor_term(arg)
        
        # elif command.startswith('properties'):
        elif 'properties'.startswith(command):
            if nargin == 1:
                return self.supported_properties
            elif arg in self.matrix_IDs:
                return self.show_matrix_properties(arg)
            else:
                return self.search_by_properties(arg)
        
        # Scan command
        elif 'scan'.startswith(command):
            self.scan_filesystem()
            print("Anymatrix scanning done.")
        
        # Sets command
        elif 'sets'.startswith(command):
            if nargin == 1:
                return self.set_IDs
            else:
                S = [[]]
                # open txt file
                with open(f"{self.root_path}/sets/{arg}.txt", 'r') as file:
                    # read file contents
                    for line in file:
                        # find lines with set members
                        if ":" in line and "%" not in line:
                            # split line into matrix ID and parameters
                            matrix_ID, parameter = line.split(':', 1)
                            S[0].append([matrix_ID, parameter.strip()])
                            
                            # parse the parameters
                            parameter = parameter.strip()
                            parameter = self.matlab_format_parser(parameter)
                            # generate matrices
                            A = self.generate_matrix(matrix_ID, parameter)
                            if type(A) is tuple:
                                S.append(A[0])
                            else:
                                S.append(A)
                return S
        # command & argument swaped.
        elif nargin > 1 and command in self.matrix_IDs and type(arg) == str and (arg == ('help') or arg ==('properties')):
            if 'help'.startswith(arg):
                self.show_matrix_help(command)
            elif 'properties'.startswith(arg):
                return self.show_matrix_properties(command)
        elif 'test'.startswith(command):
            print("group test not implemented yet.")
        else:
            return self.generate_matrix(command, varargin[1:])
    
    def test_anymatrix_properties(self, regenerate_tests:int = 0, warnings_on:int = 0, results_out:int = 0):
        self.scan_filesystem()
        
        root_path = self.root_path + '/testing'

        args = [3, 5, 8, 10, 15, 24, 25, 30, 31]
        
        # Check which properties recognized by anymatrix have tests and throw
        # warnings for those that can't be tested.
        supported_properties = []
        for prop in self.supported_properties:
            if not os.path.isfile(self.root_path + f'/testing/private/test_{prop}.py'):
                if warnings_on:
                    print(f"Test for property {prop} was not found in anymatrix.")
            else:
                supported_properties.append(prop)
        
        header = ('import sys, os\n'+
                'current = os.path.dirname(os.path.realpath(__file__))\n'+
                'parent = os.path.dirname(current)\n'+
                'sys.path.append(parent)\n'+
                'import pytest\n'+
                'from anymatrix import Anymatrix\n'+
                'from anymatrix_check_props import anymatrix_check_props\n\n'+
                '@pytest.fixture\n'+
                'def am():\n'+
                '    am = Anymatrix()\n'+
                '    return am\n\n'+
                f'supported_properties = {supported_properties}\n')
                    
        test_function_file = root_path + '/anymatrix_func_based_tests.py'
        curr_contents = ''
        if os.path.isfile(test_function_file):
            try:
                with open(test_function_file, 'r') as file:
                    curr_contents = file.read()
            except:
                return 'Error reading test function file.'
        
        # Open a file containing unit tests; if we need to regenerate the contents
        # or if the file is empty/non-existent, write in a function definition.
        if regenerate_tests or not curr_contents.startswith(header):
            mode = 'w'
        else:
            mode = 'a'
        
        with open(test_function_file, mode) as fileID:
            if mode == 'w':
                fileID.write(header)
            
            # Generate unit tests for those matrices that are found to be not present
            # in the testsuite.
            for matrix_ID in self.matrix_IDs:
                test_provided = 0
                with open(test_function_file, 'r') as file:
                    existent_test = file.read()
            
                # Check if matrix already have test function in anymatrix_func_based_tests.py
                if f"test_{matrix_ID.replace('/', '_')}" not in existent_test:
                    
                    test_file = os.path.join(self.root_path, f'{matrix_ID.split('/')[0]}/private/am_unit_tests.py')
                    
                    # If tests provided with the group, read them in.
                    if os.path.isfile(test_file):
                        with open(test_file, 'r') as file:
                            tests = file.read()
                            if f"test_{matrix_ID.replace('/', '_')}" in tests:
                                test_provided = 1
                                pattern = rf'def {f"test_{matrix_ID.replace('/', '_')}" }\(.*?\):\n(    .*\n)*'
                                function_body = re.search(pattern, tests)

                                fileID.write('\n'+function_body.group(0))
                    
                    # Otherwise, generate some tests with 0 or 1 inputs args.
                    if not test_provided:
                        ok_without_args = 1
                        try:
                            A = self.generate_matrix(matrix_ID, [])
                        except:
                            ok_without_args = 0
                        
                        if ok_without_args:
                            fileID.write(f'def test_{matrix_ID.replace("/", "_")}(am):\n')
                            fileID.write(f'    A = am.anymatrix("{matrix_ID}")\n')
                        else:
                            fileID.write(f'\n@pytest.mark.parametrize("args", {args})\n')
                            fileID.write(f'def test_{matrix_ID.replace("/", "_")}(am, args):\n')
                            fileID.write(f'    A = am.anymatrix("{matrix_ID}", args)\n')
                        fileID.write(f'    if type(A) is tuple:\n')
                        fileID.write(f'        A = A[0]\n')
                        fileID.write(f'    anymatrix_check_props(am, A, "{matrix_ID}", supported_properties)\n')

        # Execute tests
        results = pytest.main([f"{self.root_path}/testing/anymatrix_func_based_tests.py"])
        if results_out:
            return results
        else:
            return None

    def generate_test_set(self):
        self.scan_filesystem()

        default_args = [3, 5, 8, 10, 15, 24, 25, 30, 31]
                    
        test_set_file = self.root_path + '/sets/test_set.txt'
        
        with open(test_set_file, 'w') as fileID:
            
            # Generate unit tests for those matrices that are found to be not present
            # in the testsuite.
            for matrix_ID in self.matrix_IDs:
                test_provided = 0
            
                test_file = os.path.join(self.root_path, f'{matrix_ID.split('/')[0]}/private/am_unit_tests.py')
                
                # If tests provided with the group, read them in.
                if os.path.isfile(test_file):
                    with open(test_file, 'r') as file:
                        tests = file.read()
                        if f"test_{matrix_ID.replace('/', '_')}" in tests:
                            test_provided = 1
                            pattern = rf'def {f"test_{matrix_ID.replace('/', '_')}" }\(.*?\):\n(    .*\n)*'
                            match = re.search(pattern, tests)
                            if match:
                                pattern = r"am\.anymatrix\([^,]+,\s*(.*?)\)"
                                matches = re.findall(pattern, match.group(0))
                                for argument in matches:
                                    fileID.write(f'{matrix_ID}:{argument}\n')
                    
                # Otherwise, generate some tests with 0 or 1 inputs args.
                if not test_provided:
                    ok_without_args = 1
                    try:
                        A = self.generate_matrix(matrix_ID, [])
                    except:
                        ok_without_args = 0
                    
                    if ok_without_args:
                        fileID.write(f'{matrix_ID}:\n')
                    else:
                        for arg in default_args:
                            fileID.write(f'{matrix_ID}:{arg}\n')
    
    def export_test_set_to_json(self):
        result = self.anymatrix("sets", "test_set")
        np.set_printoptions(formatter={'float': '{:e}'.format})

        # Check if test set is generated.
        if result is None:
            print("Error: Test set not found. Run generate_test_set() first.")
            return

        index = result[0]
        matrices = result[1:]

        data = []
        for arg, matrix in zip(index, matrices):
            data.append({
                'matrix_ID': arg[0],
                'parameters': arg[1],
                'matrix': matrix.tolist()
            })

        with open(f"{self.root_path}/python_test_set.json", 'w') as file: 
            json.dump(data, file, indent=4)

        
import numpy as np
if __name__ == "__main__":
    root_path = os.path.dirname(os.path.abspath(__file__))
    am = Anymatrix()
    # print(am.anymatrix('properties', 'totally positive'))
    np.set_printoptions(formatter={'float': '{:e}'.format})
    print(am.anymatrix('matlab/pascal', 30)[28,29])
    
    # print(am.test_anymatrix_properties(warnings_on=0, regenerate_tests=1))
    # print(am.anymatrix("matlab/vander", "help"))
    # am.anymatrix("test")
    # am.generate_test_set()
    # am.export_test_set_to_json()