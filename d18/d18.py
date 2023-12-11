import numpy as np

def calc_surface_square_in_row(row):
    cur_val = 0
    counter = 0
    for val in row:
        if val != cur_val:
            cur_val = val
            counter += 1
    return counter + cur_val


def is_trapped_air_block(grid, pos, visited_pos):
    x, y, z = pos
    open_pos = set([pos])

    # check surrounding blocks that have not been visited yet:
    while open_pos:
        new_open_pos = set()
        for cur_pos in list(open_pos):
            x, y, z = cur_pos
            surrounding_pos = [(x - 1, y, z), (x + 1, y, z), (x, y - 1, z), (x, y + 1, z), (x, y, z - 1), (x, y, z + 1)]
            surrounding_pos = list(filter(lambda pos: visited_pos[pos[0]][pos[1]][pos[2]] == 0 and grid[pos[0]][pos[1]][pos[2]] == 0, surrounding_pos))
            for s_x, s_y, s_z in surrounding_pos:
                if s_x == 0 or s_x == grid.shape[0] - 1:
                    return False
                if s_y == 0 or s_y == grid.shape[1] - 1:
                    return False
                if s_z == 0 or s_z == grid.shape[2] - 1:
                    return False
            new_open_pos.update(surrounding_pos)        
            visited_pos[x][y][z] = 1
        open_pos = new_open_pos

    return True


def np_test(grid):
    grid[0][0][0] = 1


with open(r'C:\Users\lfrie\OneDrive\Projekte\AoC22\d18\input.txt') as f:
    lines = f.readlines()
    part = "b"

    # parse input:
    cubes = [line[:-1].split(",") for line in lines]
    cubes = [(int(cube[0]), int(cube[1]), int(cube[2])) for cube in cubes]

    # calc min and max coordinates for all points:
    x_coords = list(zip(*cubes))[0::3][0]
    y_coords = list(zip(*cubes))[1::3][0]
    z_coords = list(zip(*cubes))[2::3][0]
    min_x, max_x = min(x_coords), max(x_coords)
    min_y, max_y = min(y_coords), max(y_coords)
    min_z, max_z = min(z_coords), max(z_coords)

    # create 3d grid:
    grid = np.zeros((max_x - min_x + 1, max_y - min_y + 1, max_z - min_z + 1), int)
    for cube in cubes:
        x, y, z = cube
        grid[x - min_x][y - min_y][z - min_z] = 1


    # part b:
    if part == "b":

        # find all air trapped in lava droplet:
        trapped_air_blocks = np.zeros((max_x - min_x + 1, max_y - min_y + 1, max_z - min_z + 1), int)
        for x in range(0, max_x - min_x + 1):
            for y in range(0, max_y - min_y + 1):
                for z in range(0, max_z - min_z + 1):
                    if not (grid[x][y][z] == 1 or x == 0 or y == 0 or z == 0 or x == trapped_air_blocks.shape[0] - 1 or y == trapped_air_blocks.shape[1] - 1 or z == trapped_air_blocks.shape[1] - 1):
                        if is_trapped_air_block(grid, pos=(x, y, z), visited_pos=np.zeros((max_x - min_x + 1, max_y - min_y + 1, max_z - min_z + 1), int)):
                            trapped_air_blocks[x][y][z] = 1
        
        # fill air droplets with lava:
        grid = grid + trapped_air_blocks


    # count surface squares in x-direction:
    surface_x = 0
    for y in range(0, max_y - min_y + 1):
        for z in range(0, max_z - min_z + 1):
            row = [grid[x][y][z] for x in range(0, max_x - min_x + 1)]
            surface_x += calc_surface_square_in_row(row)

    # count surface suqares in y-direction:
    surface_y = 0
    for x in range(0, max_x - min_x + 1):
        for z in range(0, max_z - min_z + 1):
            row = [grid[x][y][z] for y in range(0, max_y - min_y + 1)]
            surface_y += calc_surface_square_in_row(row)
    
    # count surface squares in z-direction:
    surface_z = 0
    for x in range(0, max_x - min_x + 1):
        for y in range(0, max_y - min_y + 1):
            row = [grid[x][y][z] for z in range(0, max_z - min_z + 1)]
            surface_z += calc_surface_square_in_row(row)

    print("Total surface squares: " + str(surface_x + surface_y + surface_z))
    

