import numpy as np


def strength_update(sig_strength, cycle, X):
    if (cycle % 40) == 20:
        sig_strength += (cycle * X)
    cycle += 1
    return cycle, sig_strength


cycle, X, sig_strength = 0, 1, 0

with open("2022day10input.txt", "r") as f:
    for line in f:
        if line.rstrip() == 'noop':
            cycle, sig_strength = strength_update(sig_strength, cycle, X)
        else:
            inst, val = line.rstrip().split()
            cycle, sig_strength = strength_update(sig_strength, cycle, X)
            cycle, sig_strength = strength_update(sig_strength, cycle, X)
            X += int(val)

print('Part 1:', sig_strength)


def cyc_to_coord(cyc):
    cyc = cyc - 1
    col = cyc % 40
    row = int((cyc - col) / 40)
    return row, col


def sprite_coords(val, row):
    col = val % 40
    return tuple([row, val - 1]), tuple([row, val]), tuple([row, val + 1])


def screen_update(screen, cycle, X):
    row, col = cyc_to_coord(cycle)
    if tuple([row, col]) in sprite_coords(X, row):
        screen[row, col] = 1
    cycle += 1
    return cycle, screen


cycle, X, screen = 1, 1, np.zeros([6, 40]).astype(int)

with open("2022day10input.txt", "r") as f:
    for line in f:
        if line.rstrip() == 'noop':
            cycle, screen = screen_update(screen, cycle, X)
        else:
            inst, val = line.rstrip().split()
            cycle, screen = screen_update(screen, cycle, X)
            cycle, screen = screen_update(screen, cycle, X)
            X += int(val)

print('Part 2:', screen)
