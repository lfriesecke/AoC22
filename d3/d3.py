with open(r'C:\Users\lfrie\OneDrive\Projekte\AoC22\d3\input.txt') as f:
    lines = f.readlines()
    
    # task a:
    # lines = ["vJrwpWtwJgWrhcsFMMfFFhFp", "jqHRNqRjqzjGDLGLrsFMfFZSrLrFZsSL", "PmmdzqPrVvPwwTWBwg", "wMqvLMZHhHMvwLHjbvcjnnSBnvTQFn", "ttgJtRGJQctTZtZT", "CrZsJsPPZsGzwwsLwLmpwMDw"]
    splits = [(line[0:len(line)//2:], line[len(line)//2::]) for line in lines]
    duplicates = [list(set(split[0]) & set(split[1]))[0] for split in splits]
    values = [ord(dup) - ord('a') + 1 if dup.islower() else ord(dup) - ord('A') + 27 for dup in duplicates]
    print(sum(values))

    # task b:
    triples = []
    for line_no in range(0, len(lines), 3):
        triples.append((lines[line_no][:-1], lines[line_no + 1][:-1], lines[line_no + 2][:-1]))
    duplicates = [list(set(triple[0]) & set(triple[1]) & set(triple[2]))[0] for triple in triples]
    values = [ord(dup) - ord('a') + 1 if dup.islower() else ord(dup) - ord('A') + 27 for dup in duplicates]
    print(sum(values))