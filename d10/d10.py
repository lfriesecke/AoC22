import numpy as np

with open(r'C:\Users\lfrie\OneDrive\Projekte\AoC22\d10\input.txt') as f:
    lines = f.readlines()
    
    # task a:
    relevant_cycles = [20, 60, 100, 140, 180, 220]
    total_signal_strengh = 0
    current_cyle = 1
    X = 1
    for line in lines:
        words = line.split()

        # set values for execution:
        current_action = (words[0], 0)        
        executing = True

        # cycles:
        while (executing):
            # execution of current cycle:
            if current_cyle in relevant_cycles:
                total_signal_strengh += current_cyle * X

            # end of current cycle
            if current_action[0] == "noop":
                executing = False
            elif current_action[0] == "addx" and current_action[1] >= 1:
                X += int(words[1])
                executing = False
            
            # step to next cycle:
            current_action = (current_action[0], current_action[1] + 1)
            current_cyle += 1
    
    print(total_signal_strengh)

    # task b:
    num_rows = 6
    num_cols = 40
    screen = np.zeros([num_rows, num_cols], int)
    current_cyle = 1
    X = 1

    for line in lines:
        words = line.split()

        # set values for execution:
        current_action = (words[0], 0)        
        executing = True

        # cycles:
        while (executing):
            # execution of current cycle:
            crt_pos = (current_cyle - 1) % 40
            if crt_pos >= X - 1 and crt_pos <= X + 1:
                screen[(current_cyle - 1) // 40][crt_pos] = 1
            else:
                screen[(current_cyle - 1) // 40][crt_pos] = 2

            # end of current cycle
            if current_action[0] == "noop":
                executing = False
            elif current_action[0] == "addx" and current_action[1] >= 1:
                X += int(words[1])
                executing = False
            
            # step to next cycle:
            current_action = (current_action[0], current_action[1] + 1)
            current_cyle += 1

    # render result:
    image = ""
    for row in range(num_rows):
        for col in range(num_cols):
            if screen[row][col] == 1:
                image += "#"
            elif screen[row][col] == 2:
                image += "."
            else:
                raise Exception("something bad happened")
        image += "\n"
    print(image[:-1])

