import os, re

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
        self.supported_properties = []

    def scan_filesystem(self):
        self.group_IDs = self.scan_groups()
    
    def scan_sets(self):
        sets_path = os.path.join(self.root_path, 'sets')
        set_files = [f for f in os.listdir(sets_path) if f.endswith('.txt')]
        self.set_IDs = [os.path.splitext(f)[0] for f in set_files]

    # Scan the group folders and obtain the matrix IDs.
    def scan_matrices(self, groups):
        for group in groups:
            path_to_group = os.path.join(self.root_path, group, 'private')
            m_files = [f for f in os.listdir(path_to_group) if f.endswith('.py')]
            for m_file in m_files:
                with open(os.path.join(path_to_group, m_file), 'r') as file:
                    contents = file.read()
                    if 'properties = {' in contents:
                        self.matrix_IDs.append(os.path.splitext(m_file)[0])
        
        print(self.matrix_IDs)

    # Scan the root folder and obtain the group IDs.
    def scan_groups(self):
        contents = os.listdir(self.root_path)
        for items in contents:

            # Check if item is a directory.
            if os.path.isdir(items):

                # Check if item is a group directory.
                if self.is_group_dir(items):
                    self.group_IDs.append(items)

    # Check if a folder in anymatrix root directory is a group folder.
    # Group directories have one private/ directory and one file named
    # anymatrix_<dir_name>.py where <dir_name> is the directory name.
    def is_group_dir(self, directory):
        dir_path = os.path.join(self.root_path, directory)
        # Check dir has two files
        if len(os.listdir(directory)) != 2:
            return False
        # Check if anymatrix_<dir_name>.py exists
        if not os.path.isfile(os.path.join(dir_path, f'anymatrix_{directory}.py')):
            return False
        # Check if private directory exists
        if not os.path.isdir(os.path.join(dir_path, 'private')):
            return False
        return True
    
    def help(self):
        print("""ANYMATRIX  Interface for accessing the Anymatrix collections.
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
    https://doi.org/10.1007/s11075-007-9136-9""")
        
    def anymatrix(self, *args):

        nargin = len(args)

        if not self.files_scanned:
            self.scan_filesystem()
            print("Automatic anymatrix scanning done.")

        if nargin == 0:
            self.help()
            return
        
        # Parse the arguments passed to anymatrix.
        if nargin >= 2:
            for group in self.group_IDs:
                print(group)

if __name__ == "__main__":
    root_path = os.path.dirname(os.path.abspath(__file__))
    am = Anymatrix()
    am.anymatrix()
    # contents = os.listdir(root_path)
    # am.scan_groups()
    # am.scan_matrices(am.group_IDs)


    # Testing code for is_group_dir()
    # contents = os.listdir(root_path)
    # for dir in contents:
    #     if os.path.isdir(dir):
    #         print(dir)
    #         print(am.is_group_dir(dir))
        