def calc_points(c1, c2):
    val1 = ord(c1) - ord('A')
    val2 = ord(c2) - ord('X')
    return val2 + 1 + (((val2 - val1 + 1) % 3) * 3)

def calc_choice(c1, c2):
    val1 = ord(c1) - ord('A')
    val2 = ord(c2) - ord('X')
    return chr(((val1 + val2 + 2) % 3) + ord('X'))

with open(r'C:\Users\lfrie\OneDrive\Projekte\AoC22\d2\input.txt') as f:
    lines = f.readlines()
    
    # task a:
    sum = 0
    for line in lines:
        sum += calc_points(line[0], line[2])
    print("result a: " + str(sum))

    # task b:
    sum = 0
    for line in lines:
        sum += calc_points(line[0], calc_choice(line[0], line[2]))
    print("result b: " + str(sum))

    # tests:
    test_values = [('A', 'X'), ('A', 'Y'), ('A', 'Z'), ('B', 'X'), ('B', 'Y'), ('B', 'Z'), ('C', 'X'), ('C', 'Y'), ('C', 'Z')]
    for val in test_values:
        print(str(val) + " --> " + str(calc_choice(val[0], val[1])))