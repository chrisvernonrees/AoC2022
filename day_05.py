import re
import copy

def read_move(vec):
    split_vec = re.split('move | from | to | ',vec)
    output = [int(split_vec[1]),int(split_vec[2])-1,int(split_vec[3])-1]
    return(output)

crane_vec = []

with open("day5input2.txt","r") as f:
    for line in f:
        crane_vec.append(read_move(line.rstrip()))


def read_crates(crate_list):
    new_crate_list = crate_list[0:(len(crate_list) - 1)]

    indices = [1, 5, 9, 13, 17, 21, 25, 29, 33]

    stacks = []

    for i in range(len(indices)):

        stack = []

        for j in reversed(range(len(new_crate_list))):

            crate = new_crate_list[j][indices[i]]

            if (crate == ' '):
                pass
            else:
                stack.append(crate)

        stacks.append(stack)

    return (stacks)

crate_vec = []
with open("day5input1.txt","r") as f:
    for line in f:
        crate_vec.append(list(line.rstrip()))

crate_vec = read_crates(crate_vec)


def crane_move_one(crates, crane_vec):
    to_move = crane_vec[0]

    for i in range(to_move):
        moved = crates[crane_vec[1]][-1:]
        crates[crane_vec[1]] = crates[crane_vec[1]][:-1]
        crates[crane_vec[2]] += moved

    return (crates)


crate_copy = copy.deepcopy(crate_vec)

for i in range(len(crane_vec)):
    crate_copy = crane_move_one(crate_copy, crane_vec[i])

output = []
for i in range(len(crate_copy)):
    stack = crate_copy[i]
    output += stack[len(stack) - 1]
print(output)


def crane_move(crates, crane_vec):
    to_move = crane_vec[0]
    moved = crates[crane_vec[1]][-to_move:]

    crates[crane_vec[1]] = crates[crane_vec[1]][:-to_move]
    crates[crane_vec[2]] += moved

    return (crates)


crate_copy = copy.deepcopy(crate_vec)

for i in range(len(crane_vec)):
    crate_copy = crane_move(crate_copy, crane_vec[i])

output = []
for i in range(len(crate_copy)):
    stack = crate_copy[i]
    output += stack[len(stack) - 1]
print(output)