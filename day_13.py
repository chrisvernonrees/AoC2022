import ast

input_dict = {}
index = 1
l_r = []

with open("2022day13input.txt", "r") as f:
    for line in f:
        if line.rstrip() == '':
            input_dict[index] = l_r
            index += 1
            l_r = []
        else:
            l_r.append(ast.literal_eval(line.rstrip()))


def both_int(l_item, r_item):
    return (type(l_item) is int) and (type(r_item) is int)


def list_conv(l_item, r_item):
    if type(l_item) is list:
        new_l = l_item
    else:
        new_l = [l_item]
    if type(r_item) is list:
        new_r = r_item
    else:
        new_r = [r_item]
    return new_l, new_r


def right_order_rec(l_list, r_list):
    for i in range(min(len(l_list), len(r_list))):

        left, right = l_list[i], r_list[i]

        if both_int(left, right):
            if left > right:
                return 'Fail'
            elif left < right:
                return 'Pass'

        else:
            new_l, new_r = list_conv(left, right)
            if right_order_rec(new_l, new_r) == 'Fail':
                return 'Fail'
            elif right_order_rec(new_l, new_r) == 'Pass':
                return 'Pass'

    if len(l_list) > len(r_list):
        return 'Fail'
    elif len(l_list) < len(r_list):
        return 'Pass'


sum = 0
for key in input_dict:
    l, r = input_dict[key][0], input_dict[key][1]
    if right_order_rec(l, r) == 'Pass':
        sum += key

print('Part 1:', sum)

input_list = []
for key in input_dict:
    input_list += input_dict[key]


def order_packets(vec, new_item):
    for i in range(len(vec)):
        if right_order_rec(new_item, vec[i]) == 'Pass':
            vec = vec[0:i] + [new_item] + vec[i:len(vec)]
            break
    if right_order_rec(new_item, vec[len(vec) - 1]) == 'Fail':
        vec.append(new_item)
    return vec


order_vec = [[[2]], [[6]]]

for i in range(len(input_list)):
    order_vec = order_packets(order_vec, input_list[i])

decode = 1

for i in range(len(order_vec)):
    if (order_vec[i] == [[2]]) or (order_vec[i] == [[6]]):
        decode *= (i + 1)

print('Part 2:', decode)
