import numpy as np

def sim_sand(cave, pos_sand):
    sand_x, sand_y = pos_sand
    max_y = cave.shape[0]

    while sand_y < max_y - 1:
        if cave[sand_y + 1][sand_x] == 0:
            sand_y += 1
        elif cave[sand_y + 1][sand_x - 1] == 0:
            sand_y += 1
            sand_x -= 1
        elif cave[sand_y + 1][sand_x + 1] == 0:
            sand_y += 1
            sand_x += 1
            continue
        else:
            break
    
    return (sand_x, sand_y)

with open(r'C:\Users\lfrie\OneDrive\Projekte\AoC22\d14\test.txt') as f:
    lines = f.readlines()

    # exercise:
    ex = "b"

    # parse rock structures:
    rock_structs = [line[:-1].split(" -> ") for line in lines]
    rock_structs = [[(int(pair.split(",")[0]), int(pair.split(",")[1])) for pair in struct] for struct in rock_structs] 

    # find extension:
    origin = (500, 0)
    min_x, max_x, min_y, max_y = (origin[0], origin[0], origin[1], origin[1])
    for struct in rock_structs:
        for pair in struct:
            if pair[0] < min_x:
                min_x = pair[0]
            elif pair[0] > max_x:
                max_x = pair[0]
            if pair[1] > max_y:
                max_y = pair[1]
    
    if ex == "b":
        min_x = origin[0] - max_y - 1
        max_x = origin[0] + max_y + 1
    
    # init cave:
    cave_width = max_x - min_x + 3
    cave_height = max_y + 3
    cave = np.zeros((cave_height, cave_width), int)
    for struct in rock_structs:
        for i in range(len(struct) - 1):
            x1, x2, y1, y2 = (struct[i][0] - min_x + 1, struct[i+1][0] - min_x + 1, struct[i][1], struct[i+1][1])
            if y1 == y2:
                cave[y1][min([x1, x2]):max([x1, x2])+1] = 1
            else:
                for y in range(min([y1, y2]), max([y1, y2]) + 1):
                    cave[y][x1] = 1
    origin = (500 - min_x + 1, 0)

    if ex == "b":
        cave[max_y + 2][:] = 1

    # simulate sand:
    num_sand = 0

    if ex == "a":
        sand_y = 0
        while sand_y < max_y + 2:
            # simulate one block of sand:
            sand_x, sand_y = sim_sand(cave, pos_sand=origin)
            cave[sand_y][sand_x] = 2
            num_sand += 1
        num_sand -= 1
    
    else:
        sand_y = 1
        while sand_y > origin[1]:
            # simulate one block of sand:
            sand_x, sand_y = sim_sand(cave, pos_sand=origin)
            cave[sand_y][sand_x] = 2
            num_sand += 1
    
    # print cave:
    for no, row in enumerate(cave):
        print(str(no) + ": " + str(row).replace("\n", ""))
    print(num_sand)
    