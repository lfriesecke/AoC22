from filetree import FileTreeNode

with open(r'C:\Users\lfrie\OneDrive\Projekte\AoC22\d7\input.txt') as f:
    lines = f.readlines()
    
    # build file tree:
    file_tree_root = FileTreeNode(name="/", files=None, dirs=None, parent=None)
    cur_subtree = file_tree_root
    cur_line_no = 0
    while cur_line_no < len(lines):
        words = lines[cur_line_no].split()
        cur_line_no += 1

        # update files of current directory:
        if words[1] == 'ls':
            while cur_line_no < len(lines) and lines[cur_line_no][0] != '$':
                words = lines[cur_line_no].split()
                if words[0] == 'dir':
                    cur_subtree.add_dir(c_name=words[1], c_files=None, c_dirs=None)
                else:
                    cur_subtree.add_file(f_name=words[1], f_size=int(words[0]))
                cur_line_no += 1

        # change directory:
        elif words[1] == 'cd':
            if words[2] == '/':
                cur_subtree = file_tree_root
            elif words[2] == '..':
                cur_subtree = cur_subtree.get_parent()
            else:
                cur_subtree = cur_subtree.get_child(c_name=words[2])
    
    # calc total size of each directory:
    file_tree_root.update_total_file_size()
    
    # find all nodes with file size <= 100.000:
    tree_nodes = file_tree_root.get_preorder_trav()
    tree_nodes_size = [node.size_files for node in tree_nodes]
    
    # print result task a:
    print(sum([size for size in tree_nodes_size if size <= 100000]))

    # find smallest directory that frees enough space:
    needed_space = 30000000 - (70000000 - file_tree_root.size_files)
    tree_nodes_size = sorted(tree_nodes_size)
    for size in tree_nodes_size:
        if size >= needed_space:
            print(size)

