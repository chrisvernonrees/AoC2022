pri_dict_lower = {chr(i+96):i for i in range(1,27)}
pri_dict_upper = {chr(i+64):i + 26 for i in range(1,27)}
pri_dict = {**pri_dict_lower,**pri_dict_upper}

backpack_vec = []
with open("2022day3input.txt","r") as f:
    for line in f:
        backpack = list(line.rstrip())
        size = len(backpack)
        comp1 = backpack[0:int((size/2))]
        comp2 = backpack[int(-(size/2)):]
        backpack_vec.append([comp1,comp2])


def dup_check(vec):
    comp1 = vec[0]
    comp2 = vec[1]
    size = len(comp1)

    for i in range(size):
        item = comp1[i]
        if (item in comp2):
            break

    return (item)


count = 0

for i in range(len(backpack_vec)):
    backpack = backpack_vec[i]
    dup = dup_check(backpack)
    count += pri_dict[dup]

print(count)

backpack_group_vec = []
count = 0
backpack_group = []

with open("2022day3input.txt", "r") as f:
    for line in f:

        count = count + 1
        backpack = list(line.rstrip())
        backpack_group.append(backpack)

        if (count == 3):
            count = 0
            backpack_group_vec.append(backpack_group)
            backpack_group = []


def badge_check(vec):
    check_vec = vec[0] + vec[1] + vec[2]

    for i in range(len(check_vec)):
        item = check_vec[i]
        if (item in vec[0]) and (item in vec[1]) and (item in vec[2]):
            break
    return (item)

count = 0

for i in range(len(backpack_group_vec)):
    backpacks = backpack_group_vec[i]
    badge = badge_check(backpacks)
    count += pri_dict[badge]

print(count)