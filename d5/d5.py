with open(r'C:\Users\lfrie\OneDrive\Projekte\AoC22\d5\input.txt') as f:
    lines = f.readlines()
    
    # task a:
    # find stack lines:
    max_stack_line = 0
    for line in lines:
        if line == "\n":
            break
        max_stack_line += 1
    max_stack_line -= 1
    
    # build stacks:
    stacks = [[] for _ in range(0, len(lines[0]) // 4)]
    for line in lines[0:max_stack_line]:
        for block_pos in range(0, len(line), 4):
            if line[block_pos] != " ":
                stacks[block_pos // 4].append(line[block_pos+1:block_pos+2])
    for pos, stack in enumerate(stacks):
        stacks[pos] = stack[::-1]
    
    # move items:
    for line in lines[max_stack_line+2:]:
        words = line.split()
        for _ in range(int(words[1])):
            stacks[int(words[5])-1].append(stacks[int(words[3])-1].pop())
    
    # print result:
    result = ""
    for stack in stacks:
        result = result + stack[-1]
    print(result)


    # task a:
    # restore stacks:
    stacks = [[] for _ in range(0, len(lines[0]) // 4)]
    for line in lines[0:max_stack_line]:
        for block_pos in range(0, len(line), 4):
            if line[block_pos] != " ":
                stacks[block_pos // 4].append(line[block_pos+1:block_pos+2])
    for pos, stack in enumerate(stacks):
        stacks[pos] = stack[::-1]
    
    # move items:
    for line in lines[max_stack_line+2:]:
        words = line.split()
        stacks[int(words[5])-1].extend(stacks[int(words[3])-1][-int(words[1])::])
        del stacks[(int(words[3]))-1][-int(words[1])::]
    
    # print result:
    result = ""
    for stack in stacks:
        result = result + stack[-1]
    print(result)

