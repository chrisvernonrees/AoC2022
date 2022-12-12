import numpy as np

alpha_dict = {chr(i + 97): i for i in range(0, 26)}

input_list = []
with open("2022day12input.txt", "r") as f:
    for line in f:
        input_list.append(list(line.rstrip()))
input_mat = np.array(input_list)
row, col = np.shape(input_mat)

height_mat = np.zeros([row, col]).astype(int)

for i in range(row):
    for j in range(col):
        let = input_mat[i, j]
        if let == 'S':
            start = [i, j]
            height_mat[i, j] = alpha_dict['a']
        elif let == 'E':
            end = [i, j]
            height_mat[i, j] = alpha_dict['z']
        else:
            height_mat[i, j] = alpha_dict[let]

scribe_mat = np.zeros([row + 2, col + 2]).astype(int) - 1
scribe_mat[1:row + 1, 1:col + 1] = height_mat
new_start = tuple([start[0] + 1, start[1] + 1])
new_end = tuple([end[0] + 1, end[1] + 1])


def reach_check(val, check_val):
    if check_val == -1:
        return False
    else:
        return check_val >= val - 1


def reachable(mat, coord):
    reachable_coords = []
    dirs = [[1, 0], [-1, 0], [0, 1], [0, -1]]
    val = mat[coord[0], coord[1]]
    for i in range(len(dirs)):
        check_coord = [coord[0] + dirs[i][0], coord[1] + dirs[i][1]]
        check_val = mat[check_coord[0], check_coord[1]]
        if reach_check(val, check_val):
            reachable_coords.append(tuple(check_coord))
    return reachable_coords


map_dict = {}
for i in range(1, row + 1):
    for j in range(1, col + 1):
        pos = tuple([i, j])
        map_dict[pos] = reachable(scribe_mat, [i, j])


def one_step(visit_vec, maps):
    new_vec = []
    for i in range(len(visit_vec)):
        new_vec += maps[visit_vec[i]]
    return list(set(new_vec))


def steps_taken(start_points, end, maps):
    visited = [end]
    steps = 0
    redundant = [end]
    while all(point not in visited for point in start_points):
        steps += 1
        visited = one_step(visited, maps)
        visited = [i for i in visited if i not in redundant]
        redundant += visited
    return steps


nil_heights = []
h, w = np.shape(scribe_mat)
for i in range(h):
    for j in range(w):
        if scribe_mat[i, j] == 0:
            nil_heights.append(tuple([i, j]))

print('Part 1:', steps_taken([new_start], new_end, map_dict))
print('Part 2:', steps_taken(nil_heights, new_end, map_dict))

