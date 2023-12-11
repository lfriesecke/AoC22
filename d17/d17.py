import numpy as np

class Rock:
    def __init__(self, pos, shape_pos):
        self.pos = pos
        self.shape_pos = shape_pos
    
    def simulate_movement(self, chamber, dir_vec):
        # calc new positions:
        new_pos = (self.pos[0] + dir_vec[0], self.pos[1] + dir_vec[1])
        abs_pos = [(new_pos[0] + pos[0], new_pos[1] + pos[1]) for pos in self.shape_pos]

        # check if new positions are valid:
        max_y, max_x = chamber.shape
        for pos in abs_pos:
            if pos[0] < 0 or pos[0] >= max_x or pos[1] < 0 or pos[1] >= max_y:
                return False
            if chamber[pos[1]][pos[0]] == 1:
                return False
        
        # update position:
        self.pos = new_pos
        return True
    
    def get_max_y(self):
        abs_y = [self.pos[1] + pos[1] for pos in self.shape_pos]
        return max(abs_y)



def simulate_rock(chamber, cur_height, rock, movements, cur_movement_id):

    # spawn rock:
    rock.pos = (2, cur_height + 4)

    # simulate rock:
    while True:
        # horizontal_movement:
        rock.simulate_movement(chamber, (movements[cur_movement_id], 0))
        cur_movement_id = (cur_movement_id + 1) % len(movements)

        # vertical:movement:
        suc_move = rock.simulate_movement(chamber, (0, -1))
        if not suc_move:
            break

    # calc new height and update chamber:
    new_height = max(cur_height, rock.get_max_y())
    for x, y in [(rock.pos[0] + rel_pos[0], rock.pos[1] + rel_pos[1]) for rel_pos in rock.shape_pos]:
        chamber[y][x] = 1

    return (new_height, cur_movement_id)


with open(r'C:\Users\lfrie\OneDrive\Projekte\AoC22\d17\input.txt') as f:
    lines = f.readlines()

    # parse input:
    movements = np.array([1 if char == '>' else -1 for char in lines[0][:-1]], int)

    # init rock objects:
    rocks = [
        Rock(pos=[-1, -1], shape_pos=((0, 0), (1, 0), (2, 0), (3, 0))),
        Rock(pos=[-1, -1], shape_pos=((0, 1), (1, 0), (1, 1), (1, 2), (2, 1))),
        Rock(pos=[-1, -1], shape_pos=((0, 0), (1, 0), (2, 0), (2, 1), (2, 2))),
        Rock(pos=[-1, -1], shape_pos=((0, 0), (0, 1), (0, 2), (0, 3))),
        Rock(pos=[-1, -1], shape_pos=((0, 0), (0, 1), (1, 0), (1, 1)))
    ]
    
    # simulate falling rocks:
    upper_limit = 100000
    chamber = np.zeros((upper_limit, 7), int)
    chamber[0][0:7] = 1
    num_rocks = 50000
    cur_height = 0
    cur_movement_id = 0

    for cur_rock_num in range(num_rocks):
        print(str(cur_rock_num) + " : " + str(cur_rock_num % 5) + " : " + str(cur_movement_id))

        cur_height, cur_movement_id = simulate_rock(
            chamber=chamber,
            cur_height=cur_height,
            rock=rocks[cur_rock_num % len(rocks)],
            movements=movements,
            cur_movement_id=cur_movement_id
        )

    # save full result:
    output = ""
    for row in chamber[::-1]:
        output += str(row) + "\n"
    file = open(r'C:\Users\lfrie\OneDrive\Projekte\AoC22\d17\output.txt', 'w')
    file.write(output)
    file.close
    
    # print result:
    print(cur_height)
