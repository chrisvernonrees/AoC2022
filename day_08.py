import numpy as np

input_list = []
with open("2022day8input.txt","r") as f:
    for line in f:
        input_list.append(list(line.rstrip()))

input_mat = np.asarray(input_list).astype(int)

def edge_check(mat, row, col):
    flag = 0
    max_row, max_col = np.shape(mat)
    if (row == 0) or (row == max_row - 1) or (col == 0) or (col == max_col - 1):
        flag = 1
    return(flag)

def vis_check(mat, row, col):
    flag = 0
    up_height = max(mat[:row,col])
    down_height = max(mat[row+1:,col])
    left_height = max(mat[row,:col])
    right_height = max(mat[row,col+1:])
    if (mat[row, col] > min(up_height, down_height, left_height, right_height)):
        flag = 1
    return(flag)

def score_calc(vec, val):
    score = 0
    for i in range(len(vec)):
        score += 1
        if (vec[i] >= val):
            break
    return(score)


def scenic_score(mat, row, col):
    my_height = mat[row, col]

    up_vec = np.flip(mat[:row, col])
    down_vec = mat[row + 1:, col]
    left_vec = np.flip(mat[row, :col])
    right_vec = mat[row, col + 1:]

    up_score = score_calc(up_vec, my_height)
    down_score = score_calc(down_vec, my_height)
    left_score = score_calc(left_vec, my_height)
    right_score = score_calc(right_vec, my_height)

    score = up_score * down_score * left_score * right_score

    return (score)

row_size, col_size = np.shape(input_mat)
check_mat = np.zeros([row_size, col_size]).astype(int)
score_mat = np.zeros([row_size, col_size]).astype(int)

for row in range(row_size):
    for col in range(col_size):
        if edge_check(input_mat, row, col) == 1:
            check_mat[row, col] = 1
            score_mat[row, col] = 0
        else:
            check_mat[row,col] = vis_check(input_mat, row, col)
            score_mat[row,col] = scenic_score(input_mat, row, col)

print(sum(sum(check_mat)))
print(score_mat.max())