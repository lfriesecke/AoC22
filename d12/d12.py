import numpy as np

def parse_char(char):
    if char == "E":
        return 26
    elif char == "S":
        return 1
    else:
        return ord(char) - ord('a')

def calc_distance_a(heights, start_pos):

    # init values:
    num_rows, num_cols = heights.shape
    distances = np.ones((num_rows, num_cols), int) * (-1)
    distances[start_pos[0]][start_pos[1]] = 0
    cur_travs = {start_pos}

    # breadth first search:
    while cur_travs:
        next_travs = set()
        for cur_pos in cur_travs:
            reach_positions = {(cur_pos[0] + 1, cur_pos[1]), (cur_pos[0], cur_pos[1] + 1), (cur_pos[0] - 1, cur_pos[1]), (cur_pos[0], cur_pos[1] - 1)}
            for reach_pos in reach_positions:
                if reach_pos[0] >= 0 and reach_pos[0] < num_rows and reach_pos[1] >= 0 and reach_pos[1] < num_cols and heights[reach_pos[0]][reach_pos[1]] <= heights[cur_pos[0]][cur_pos[1]] + 1:
                    if (distances[reach_pos[0]][reach_pos[1]] < 0) or (distances[reach_pos[0]][reach_pos[1]] > distances[cur_pos[0]][cur_pos[1]] + 1):
                        distances[reach_pos[0]][reach_pos[1]] = distances[cur_pos[0]][cur_pos[1]] + 1
                        next_travs.add(reach_pos)
        cur_travs = next_travs
    
    # return result:
    return distances

def calc_distance_b(heights, target_pos):

    # init values:
    num_rows, num_cols = heights.shape
    distances = np.ones((num_rows, num_cols), int) * (-1)
    distances[target_pos[0]][target_pos[1]] = 0
    cur_travs = {target_pos}

    # breadh first search:
    while cur_travs:
        next_travs = set()
        for cur_pos in cur_travs:
            reach_positions = {(cur_pos[0] + 1, cur_pos[1]), (cur_pos[0], cur_pos[1] + 1), (cur_pos[0] - 1, cur_pos[1]), (cur_pos[0], cur_pos[1] - 1)}
            for reach_pos in reach_positions:
                if reach_pos[0] >= 0 and reach_pos[0] < num_rows and reach_pos[1] >= 0 and reach_pos[1] < num_cols and heights[cur_pos[0]][cur_pos[1]] <= heights[reach_pos[0]][reach_pos[1]] + 1:
                    if (distances[reach_pos[0]][reach_pos[1]] < 0) or (distances[reach_pos[0]][reach_pos[1]] > distances[cur_pos[0]][cur_pos[1]] + 1):
                        distances[reach_pos[0]][reach_pos[1]] = distances[cur_pos[0]][cur_pos[1]] + 1
                        next_travs.add(reach_pos)
        cur_travs = next_travs
    
    # return result:
    return distances


with open(r'C:\Users\lfrie\OneDrive\Projekte\AoC22\d12\input.txt') as f:
    lines = f.readlines()

    # parse input:
    heights = np.zeros((len(lines), len(lines[0][:-1])), int)
    start_pos = ()
    target_pos = ()
    for num_r, line in enumerate(lines):
        for num_c, char in enumerate(line[:-1]):
            heights[num_r][num_c] = parse_char(char)
            if char == 'S':
                start_pos = (num_r, num_c)
            elif char == 'E':
                target_pos = (num_r, num_c)
    
    # task a:
    distances = calc_distance_a(heights, start_pos)
    print(distances[target_pos[0]][target_pos[1]])

    # task b:
    distances = calc_distance_b(heights, target_pos)
    min_heights = []
    for row_num, row in enumerate(heights):
        for col_num, height in enumerate(row):
            if height == 0 and distances[row_num][col_num] > 0:
                min_heights.append(distances[row_num][col_num])
    print(min(min_heights))
    