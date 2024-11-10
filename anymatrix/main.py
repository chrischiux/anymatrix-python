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
        
    def anymatrix(self, command, *args):
        if not self.files_scanned:
            print("Scanning filesystem...")
        
        print("Anymatrix command: ", command)

if __name__ == "__main__":
    root_path = os.path.dirname(os.path.abspath(__file__))
    am = Anymatrix()
    contents = os.listdir(root_path)
    am.scan_groups()
    am.scan_matrices(am.group_IDs)


    # Testing code for is_group_dir()
    # contents = os.listdir(root_path)
    # for dir in contents:
    #     if os.path.isdir(dir):
    #         print(dir)
    #         print(am.is_group_dir(dir))
        