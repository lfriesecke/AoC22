with open(r'C:\Users\lfrie\OneDrive\Projekte\AoC22\d6\input.txt') as f:
    line = f.readlines()[0][:-1]
    SEQUENCE_LENGTH = 14

    # init sequence:
    cur_sequence = []
    for pos in range(0, SEQUENCE_LENGTH):
        cur_sequence.append(line[pos])
    
    # iterate over line:
    marker_pos = 0
    for char in line:
        if len(set(cur_sequence)) == SEQUENCE_LENGTH:
            break
        del cur_sequence[0]
        cur_sequence.append(char)
        marker_pos += 1
    
    print(marker_pos)
