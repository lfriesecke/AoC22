import numpy as np

kgV = 9699690
# kgV = 96577

def calc_operation(value, operation, operation_num):
    if operation == "+":
        return value + operation_num
    elif operation == "*":
        return value * operation_num
    elif operation == "^":
        return value ** operation_num
    return None


class Monkey:
    def __init__(self, current_items, operation, operation_num, divisible_by, monkey_true, monkey_false):
        self.current_items = current_items
        self.operation = operation
        self.operation_num = operation_num
        self.divisible_by = divisible_by
        self.monkey_true = monkey_true
        self.monkey_false = monkey_false
        self.num_inspected_items = 0

    def inspect_items(self, monkeys):
        for cur_item in self.current_items:
            self.num_inspected_items += 1
            cur_worry_level = calc_operation(value=cur_item, operation=self.operation, operation_num=self.operation_num) % kgV
            if cur_worry_level % self.divisible_by == 0:
                monkeys[self.monkey_true].current_items.append(cur_worry_level)
            else:
                monkeys[self.monkey_false].current_items.append(cur_worry_level)
        self.current_items = []


with open(r'C:\Users\lfrie\OneDrive\Projekte\AoC22\d11\input.txt') as f:
    lines = f.readlines()

    # init monkeys:
    LINES_PER_MONKEY = 7
    monkeys = []
    for monkey_no in range((len(lines) + 1) // LINES_PER_MONKEY):
        current_items = [int(item) for item in lines[monkey_no * LINES_PER_MONKEY + 1].replace(',', '').split()[2::]]
        operation = lines[monkey_no * LINES_PER_MONKEY + 2].split()[4]
        operation_num = lines[monkey_no * LINES_PER_MONKEY + 2].split()[5]
        divisible_by = int(lines[monkey_no * LINES_PER_MONKEY + 3].split()[3])
        monkey_true = int(lines[monkey_no * LINES_PER_MONKEY + 4].split()[5])
        monkey_false = int(lines[monkey_no * LINES_PER_MONKEY + 5].split()[5])
        monkeys.append(Monkey(current_items, operation, operation_num, divisible_by, monkey_true, monkey_false))
    monkeys[3].operation = '^'          # (monkey 3 is special)
    monkeys[3].operation_num = 2
    # monkeys[2].operation = '^'          # (monkey 2 is special)
    # monkeys[2].operation_num = 2
    for monkey in monkeys:
        monkey.operation_num = int(monkey.operation_num)

    # tasks:
    NUM_ROUNDS = 10000
    for i in range(NUM_ROUNDS):
        for monkey in monkeys:
            monkey.inspect_items(monkeys)
        # print("After round " + str(i + 1) + ":")
        # for num, monkey in enumerate(monkeys):
            # print("Monkey " + str(num) + ": " + str(monkey.current_items))
        
    num_inspections = sorted([monkey.num_inspected_items for monkey in monkeys])
    print(num_inspections)
    print(num_inspections[-1] * num_inspections[-2])

