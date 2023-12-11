import numpy as np

def calc_tail_movement(rel_position_head):
    # calc L-infty distance:
    distance = max([abs(rel_position_head[0]), abs(rel_position_head[1])])

    # case 1: movement needed:
    if distance == 2:
        # case 1.1: horizontal movement
        if rel_position_head[1] == 0:
            return (rel_position_head[0] // 2, 0)
        # case 1.2: vertikal movement
        elif rel_position_head[0] == 0:
            return (0, rel_position_head[1] // 2)
        # case 1.3: movement on secondary diagonal:
        elif (rel_position_head[0] > 0 and rel_position_head[1] > 0) or (rel_position_head[0] < 0 and rel_position_head[1] < 0):
            return (rel_position_head[0] // abs(rel_position_head[0]), rel_position_head[0] // abs(rel_position_head[0]))
        # case 1.4: movement on main diagonal:
        elif (rel_position_head[0] > 0 and rel_position_head[1] < 0) or (rel_position_head[0] < 0 and rel_position_head[1] > 0):
            return (rel_position_head[0] // abs(rel_position_head[0]), - rel_position_head[0] // abs(rel_position_head[0]))

    # case 2: no movement needed
    return (0, 0)

def update_positions(positions_knots, direction):
    # update position of head:
    if direction == 'U':
        positions_knots[0] = (positions_knots[0][0], positions_knots[0][1] + 1)
    elif direction == 'D':
        positions_knots[0] = (positions_knots[0][0], positions_knots[0][1] - 1)
    elif direction == 'R':
        positions_knots[0] = (positions_knots[0][0] + 1, positions_knots[0][1])
    elif direction == 'L':
        positions_knots[0] = (positions_knots[0][0] - 1, positions_knots[0][1])
    else:
        return None
    
    # update positions of other knots:
    for knot_index in range(1, len(position_knots)):
        dx, dy = calc_tail_movement(rel_position_head=(position_knots[knot_index - 1][0] - position_knots[knot_index][0], position_knots[knot_index - 1][1] - position_knots[knot_index][1]))
        position_knots[knot_index] = (position_knots[knot_index][0] + dx, position_knots[knot_index][1] + dy)
    
    return position_knots


with open(r'C:\Users\lfrie\OneDrive\Projekte\AoC22\d9\input.txt') as f:
    lines = f.readlines()
    
    # task a:
    num_knots = 2
    num_cells = 1000
    position_knots = [(num_cells // 2, num_cells // 2) for _ in range(num_knots)]
    traveled_positions = np.zeros((num_cells, num_cells), int)
    traveled_positions[num_cells // 2][num_cells // 2] = 1

    for step in lines:
        direction, num_steps = step.split()
        for _ in range(int(num_steps)):
            position_knots = update_positions(position_knots, direction)
            traveled_positions[position_knots[num_knots - 1][0]][position_knots[num_knots - 1][1]] = 1
    
    print(sum(sum(traveled_positions)))


    # task b:
    num_knots = 10
    num_cells = 1000
    position_knots = [(num_cells // 2, num_cells // 2) for _ in range(num_knots)]
    traveled_positions = np.zeros((num_cells, num_cells), int)
    traveled_positions[num_cells // 2][num_cells // 2] = 1

    for step in lines:
        direction, num_steps = step.split()
        for _ in range(int(num_steps)):
            position_knots = update_positions(position_knots, direction)
            traveled_positions[position_knots[num_knots - 1][0]][position_knots[num_knots - 1][1]] = 1
    
    print(sum(sum(traveled_positions)))
