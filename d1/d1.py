with open(r'C:\Users\lfrie\OneDrive\Projekte\AoC22\d1\input.txt') as f:
    # init values:
    lines = f.readlines()
    cals_elves = []

    # count cals for each elf:
    cals_cur_elf = 0
    for line in lines:
        line = line[:-1]
        if line == "":
            cals_elves.append(cals_cur_elf)
            cals_cur_elf = 0
        else:
            cals_cur_elf += int(line)
    
    # print maximum numbers of calories:
    print(max(cals_elves))

    # print total numbers of calories of top three elves:
    cals_elves = sorted(cals_elves)
    print(cals_elves[-1] + cals_elves[-2] + cals_elves[-3])
