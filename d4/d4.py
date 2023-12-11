with open(r'C:\Users\lfrie\OneDrive\Projekte\AoC22\d4\input.txt') as f:
    lines = f.readlines()
    
    # task a:
    splits_elves = [line[:-1:].split(",") for line in lines]
    splits = [(split[0].split("-"), split[1].split("-")) for split in splits_elves]
    splits = [((int(split[0][0]), int(split[0][1])), (int(split[1][0]), int(split[1][1]))) for split in splits]
    reconsiderations = filter(lambda pair: (pair[0][0] <= pair[1][0] and pair[0][1] >= pair[1][1]) or (pair[0][0] >= pair[1][0] and pair[0][1] <= pair[1][1]), splits)
    print(len(list(reconsiderations)))

    # task b:
    reconsiderations = filter(lambda pair: not(pair[0][1] < pair[1][0] or pair[1][1] < pair[0][0]), splits)
    print(len(list(reconsiderations)))
