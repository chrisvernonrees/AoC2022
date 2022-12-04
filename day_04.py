import re

def pair_split(vec):
    split_vec = re.split('-|,',vec)
    output_vec = [[int(split_vec[0]),int(split_vec[1])],[int(split_vec[2]),int(split_vec[3])]]
    return(output_vec)

pair_vec = []

with open("2022day4input.txt","r") as f:
    for line in f:
        pair_vec.append(pair_split(line))


def cont_check(pairs):
    pair11 = pairs[0][0]
    pair12 = pairs[0][1]
    pair21 = pairs[1][0]
    pair22 = pairs[1][1]

    cont_flag = 0

    if (pair11 >= pair21) and (pair12 <= pair22):
        cont_flag = 1
    elif (pair21 >= pair11) and (pair22 <= pair12):
        cont_flag = 1

    return (cont_flag)


count = 0

for i in range(len(pair_vec)):
    count += cont_check(pair_vec[i])

print(count)


def olap_check(pairs):
    sorted_pairs = sorted(pairs, key=lambda x: x[0])

    pair1 = sorted_pairs[0]
    pair2 = sorted_pairs[1]

    if (min(pair2) > max(pair1)):
        olap_flag = 0
    else:
        olap_flag = 1

    return (olap_flag)


count = 0

for i in range(len(pair_vec)):
    count += olap_check(pair_vec[i])

print(count)