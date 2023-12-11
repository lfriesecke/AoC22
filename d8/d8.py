import numpy as np

def calc_viewing_distance(heights, x, y, max_x, max_y):
    h = heights[y][x]

    # check upper trees:
    upper_trees = 1
    cur_y = y - 1
    while cur_y > 0 and heights[cur_y][x] < h:
        upper_trees += 1
        cur_y -= 1
    
    # check lower trees:
    lower_trees = 1
    cur_y = y + 1
    while cur_y < max_y and heights[cur_y][x] < h:
        lower_trees += 1
        cur_y += 1
    
    # check left trees:
    left_trees = 1
    cur_x = x - 1
    while cur_x > 0 and heights[y][cur_x] < h:
        left_trees += 1
        cur_x -= 1

    # check right trees:
    right_trees = 1
    cur_x = x + 1
    while cur_x < max_x and heights[y][cur_x] < h:
        right_trees += 1
        cur_x += 1
    
    return (upper_trees, lower_trees, left_trees, right_trees)


with open(r'C:\Users\lfrie\OneDrive\Projekte\AoC22\d8\input.txt') as f:
    lines = f.readlines()
    
    # task a:

    # create numpy arrays:
    num_rows = len(lines)
    num_cols = len(lines[0]) - 1
    heights = np.array([list(line[:-1]) for line in lines]).astype(int)
    valid_trees = np.zeros((num_rows, num_cols)).astype(int)

    # check rows from left:
    for cur_y in range(0, num_rows):
        cur_max_height = -1
        for cur_x in range(0, num_cols):
            if heights[cur_y][cur_x] > cur_max_height:
                cur_max_height = heights[cur_y][cur_x]
                valid_trees[cur_y][cur_x] = 1
            if cur_max_height >= 9:
                break
    
    # check rows from right:
    for cur_y in range(0, num_rows):
        cur_max_height = -1
        for cur_x in range(num_cols - 1, -1, -1):
            if heights[cur_y][cur_x] > cur_max_height:
                cur_max_height = heights[cur_y][cur_x]
                valid_trees[cur_y][cur_x] = 1
            if cur_max_height >= 9:
                break
    
    # check cols from top:
    for cur_x in range(0, num_cols):
        cur_max_height = -1
        for cur_y in range(0, num_rows):
            if heights[cur_y][cur_x] > cur_max_height:
                cur_max_height = heights[cur_y][cur_x]
                valid_trees[cur_y][cur_x] = 1
            if cur_max_height >= 9:
                break
    
    # check cols from bottom:
    for cur_x in range(0, num_cols):
        cur_max_height = -1
        for cur_y in range(num_rows - 1, -1, -1):
            if heights[cur_y][cur_x] > cur_max_height:
                cur_max_height = heights[cur_y][cur_x]
                valid_trees[cur_y][cur_x] = 1
            if cur_max_height >= 9:
                break

    print(sum(sum(valid_trees)))


    # task b:

    max_viewing_score = 0
    best_x = -1
    best_y = -1
    for cur_x in range(1, num_cols - 1):
        for cur_y in range(1, num_rows - 1):
            a, b, c, d = calc_viewing_distance(heights, x=cur_x, y=cur_y, max_x=num_cols - 1, max_y=num_rows - 1)
            viewing_score = a * b * c * d
            if viewing_score > max_viewing_score:
                max_viewing_score = viewing_score
                best_x = cur_x
                best_y = cur_y
    
    print(max_viewing_score)

