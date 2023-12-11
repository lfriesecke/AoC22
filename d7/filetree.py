class FileTreeNode:

    # constructor:
    def __init__(self, name, files = None, dirs = None, parent = None):
        self.name = name
        
        self.files = files
        if files is None:
            self.files = {}
        
        self.dirs = dirs
        if dirs is None:
            self.dirs = {}
        
        self.parent = parent
        self.size_files = 0
    
    def add_dir(self, c_name, c_files = None, c_dirs = None):
        child = FileTreeNode(name=c_name, files=c_files, dirs=c_dirs, parent=self)
        self.dirs[c_name] = child
    
    def add_file(self, f_name, f_size):
        self.files[f_name] = f_size

    def get_child(self, c_name):
        return self.dirs.get(c_name)
    
    def get_parent(self):
        return self.parent
    
    def is_leaf(self):
        return len(self.dirs.keys()) == 0
    
    def calc_size_files(self):
        return sum(self.files.values())
    
    def update_total_file_size(self):

        size_files = self.calc_size_files()
        
        # add size of child dirs::
        if not self.is_leaf():
            for child in self.dirs.values():
                child.update_total_file_size()
                size_files += child.size_files
        
        # update attribute:
        self.size_files = size_files
    
    def get_preorder_trav(self):
        if self.is_leaf():
            return [self]
        trav = []
        for child in self.dirs.values():
            trav.extend(child.get_preorder_trav())
        trav.append(self)
        return trav
            
