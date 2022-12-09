import numpy as np

dir_dict = {'U': np.array([1, 0]), 'D': np.array([-1, 0]), 'L': np.array([0, -1]), 'R': np.array([0, 1])}


def pos_neg(val):
    if val < 1:
        return -1
    else:
        return 1


def knot_move(head_pos, tail_pos):
    v_var = head_pos[0] - tail_pos[0]
    h_var = head_pos[1] - tail_pos[1]

    if (abs(v_var) + abs(h_var)) > 2:
        v_move = 1 * pos_neg(v_var)
        h_move = 1 * pos_neg(h_var)
    else:
        v_move = max(abs(v_var) - 1, 0) * pos_neg(v_var)
        h_move = max(abs(h_var) - 1, 0) * pos_neg(h_var)

    return np.array([v_move, h_move])


h_pos = np.array([0, 0])
t_pos = np.array([0, 0])
t_pos_list = []

with open("2022day9input.txt", "r") as f:
    for line in f:

        direct, dist = line.rstrip().split()

        for i in range(int(dist)):
            h_pos += dir_dict[direct]
            t_pos += knot_move(h_pos, t_pos)

            if t_pos.tolist() not in t_pos_list:
                t_pos_list.append(t_pos.tolist())

print('Part 1:', len(t_pos_list))

rope_len = 10

rope = []
for i in range(rope_len):
    rope.append(np.array([0, 0]))


def rope_move(rope, direct, rope_len):
    rope[0] += dir_dict[direct]

    for i in range(1, rope_len):
        t, h = rope[i], rope[i - 1]
        rope[i] += knot_move(h, t)

    return rope


t_pos_list = []

with open("2022day9input.txt", "r") as f:
    for line in f:
        direct, dist = line.rstrip().split()

        for i in range(int(dist)):
            rope = rope_move(rope, direct, rope_len)
            t_pos = (rope[rope_len - 1]).tolist()

            if t_pos not in t_pos_list:
                t_pos_list.append(t_pos)

print('Part 2:', len(t_pos_list))
