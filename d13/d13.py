from functools import cmp_to_key

def split_string(str):

    entrys = []
    num_open_brackets = 0
    last_pos = 0

    # split string:
    for pos, char in enumerate(str):
        if char == '[':
            num_open_brackets += 1
        elif char == ']':
            num_open_brackets -= 1
        elif char == ',' and num_open_brackets == 0:
            entrys.append(str[last_pos:pos])
            last_pos = pos + 1
    entrys.append(str[last_pos:])

    return entrys


def parse_line(line):

    # special case: list is empty:
    if len(line) == 0:
        return []

    # convert current string to list:
    line = split_string(line)

    # convert strings in list to right items:
    for pos, str in enumerate(line):
        if str[0] == '[' and str[-1] == ']':
            line[pos] = parse_line(str[1:-1])
        else:
            line[pos] = int(str)

    return line


def pair_is_valid(pair):
    length = max([len(pair[0]), len(pair[1])])
    
    for pos in range(length):
        # case 1: one list is shorter:
        if pos >= len(pair[0]):
            return True
        if pos >= len(pair[1]):
            return False

        # case 2: both values are integers:
        if isinstance(pair[0][pos], int) and isinstance(pair[1][pos], int):
            if pair[0][pos] < pair[1][pos]:
                return True
            elif pair[0][pos] > pair[1][pos]:
                return False
        
        # case 3: both values are lists:
        elif isinstance(pair[0][pos], list) and isinstance(pair[1][pos], list):
            res = pair_is_valid((pair[0][pos], pair[1][pos]))
            if res is not None:
                return res
        
        # case 4: one value is list
        else:
            if isinstance(pair[0][pos], int):
                res = pair_is_valid(([pair[0][pos]], pair[1][pos]))
            else:
                res = pair_is_valid((pair[0][pos], [pair[1][pos]]))
            if res is not None:
                return res

    return None


def compare_packets(packet1, packet2):
    if pair_is_valid((packet1, packet2)):
        return 1
    else:
        return -1



with open(r'C:\Users\lfrie\OneDrive\Projekte\AoC22\d13\input.txt') as f:
    lines = f.readlines()

    # task a - parse input:
    pairs = []
    for pos_line in range(0, len(lines) + 1, 3):
        pairs.append((parse_line(lines[pos_line][:-1]), parse_line(lines[pos_line + 1][:-1])))

    # sum up valid pair indices:
    sum = 0
    for index, pair in enumerate(pairs):
        if pair_is_valid(pair):
            sum += index + 1
    
    # print result:
    print(sum)

    # task b - rearrange packets:
    packets = []
    for pair in pairs:
        packets.extend(list(pair))
    packets.extend([[[[2]]], [[[6]]]])
    packets = [pack[0] for pack in packets]
    
    # sort packets and find decoder keys:
    packets = sorted(packets, reverse=True, key=cmp_to_key(compare_packets))
    div_1 = [[2]]
    div_2 = [[6]]
    for index, pack in enumerate(packets):
        if pack == div_1:
            pos_div_1 = index + 1
        elif pack == div_2:
            pos_div_2 = index + 1

    # print result:
    print(pos_div_1 * pos_div_2)
    