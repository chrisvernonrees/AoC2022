import copy

monkey_items = []
monkey_op = {}
monkey_test = {}

monkey = 0
op_vec = []

with open("2022day11input.txt", "r") as f:

    for line in f:
        if line == '\n':
            monkey_test[monkey] = op_vec
            op_vec = []
            monkey += 1
        elif 'Starting items: ' in line:
            items = line.replace('Starting items: ', '').strip().split(', ')
            item_list = list(map(int, items))
            monkey_items.append(item_list)
        elif 'Test: divisible by ' in line:
            op_vec.append(int(line.replace('Test: divisible by ', '').strip()))
        elif 'If true: throw to monkey ' in line:
            op_vec.append(int(line.replace('If true: throw to monkey ', '').strip()))
        elif 'If false: throw to monkey ' in line:
            op_vec.append(int(line.replace('If false: throw to monkey ', '').strip()))
        elif 'Operation: new = old ' in line:
            monkey_op[monkey] = line.replace('Operation: new = old ', '').strip().split()

monkey_items_2 = copy.deepcopy(monkey_items)

mod = 1
for monkey in range(len(monkey_test)):
    mod *= monkey_test[monkey][0]


def inspect(item, op_vec):
    if op_vec[1] == 'old':
        val = item
    else:
        val = int(op_vec[1])

    if op_vec[0] == '+':
        return int((item + val) / 3)
    elif op_vec[0] == '*':
        return int((item * val) / 3)


def inspect_2(item, op_vec, mod):
    if op_vec[1] == 'old':
        val = item
    else:
        val = int(op_vec[1])

    if op_vec[0] == '+':
        return (item + val) % mod
    elif op_vec[0] == '*':
        return (item * val) % mod


def monkey_pass(monkey, monkey_items, new_val, test_vec):

    if new_val % test_vec[0] == 0:
        monkey_items[test_vec[1]].append(new_val)
    else:
        monkey_items[test_vec[2]].append(new_val)

    monkey_items[monkey] = monkey_items[monkey][1:]

    return monkey_items

def monkey_search(monkey, monkey_items, op_vec, test_vec):
    while len(monkey_items[monkey]) > 0:
        item = monkey_items[monkey][0]
        new_val = inspect(item, op_vec)
        monkey_items = monkey_pass(monkey, monkey_items, new_val, test_vec)
    return monkey_items

def monkey_search_2(monkey, monkey_items, op_vec, test_vec, mod):
    while len(monkey_items[monkey]) > 0:
        item = monkey_items[monkey][0]
        new_val = inspect_2(item, op_vec, mod)
        monkey_items = monkey_pass(monkey, monkey_items, new_val, test_vec)
    return monkey_items


passes = 20
inspect_vec = [0] * len(monkey_items)

for i in range(passes):
    for monkey in range(len(monkey_items)):
        inspect_vec[monkey] += len(monkey_items[monkey])

        op_vec = monkey_op[monkey]
        test_vec = monkey_test[monkey]
        monkey_items = monkey_search(monkey, monkey_items, op_vec, test_vec)

print('Part 1', sorted(inspect_vec)[-1]*sorted(inspect_vec)[-2])

passes = 10000
inspect_vec = [0] * len(monkey_items_2)

for i in range(passes):
    for monkey in range(len(monkey_items_2)):
        inspect_vec[monkey] += len(monkey_items_2[monkey])

        op_vec = monkey_op[monkey]
        test_vec = monkey_test[monkey]
        monkey_items_2 = monkey_search_2(monkey, monkey_items_2, op_vec, test_vec, mod)

print('Part 2', sorted(inspect_vec)[-1]*sorted(inspect_vec)[-2])