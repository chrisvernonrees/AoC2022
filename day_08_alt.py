import numpy as np

input_list = []
with open("2022day8input.txt","r") as f:
    for line in f:
        input_list.append(list(line.rstrip()))

input_mat = np.asarray(input_list).astype(int)

def tree_lines(mat,row,col):
    val = mat[row,col]
    u = np.flip(mat[:row,col])
    d = mat[row+1:,col]
    l = np.flip(mat[row,:col])
    r = mat[row,col+1:]
    return(val,[u,d,l,r])

def stop_and_score(val, vec):
    for i in range(len(vec)):
        if (vec[i] >= val):
            return(1, i+1)
            break
    return(0, len(vec))

def surround_and_scenic(val, lines):
    count = 0
    tot_score = 1
    for i in range(len(lines)):
        stop, score = stop_and_score(val, lines[i])
        count += stop
        tot_score *= score
    return(int(count != 4), tot_score)

row_size, col_size = np.shape(input_mat)
vis_mat = np.ones([row_size, col_size]).astype(int)
score_mat = np.zeros([row_size, col_size]).astype(int)

for row in range(1, row_size - 1):
    for col in range(1, col_size - 1):
        val, lines = tree_lines(input_mat, row, col)
        vis, score = surround_and_scenic(val, lines)
        vis_mat[row, col] = vis
        score_mat[row, col] = score

print('Part 1:', vis_mat.sum())
print('Part 2:', score_mat.max())
