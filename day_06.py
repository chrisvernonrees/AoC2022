input_vec = []

with open("2022day6input.txt","r") as f:
    for line in f:
        input_vec += list(line.rstrip())

def uniq_check(vec):
    flag = 1
    for item in vec:
        if vec.count(item) > 1:
            flag = 0
            break
    return(flag)

def start_of_marker(input_vec,size):
    for i in range(size,len(input_vec)-1):
        check_vec = input_vec[i-size:i]
        if (uniq_check(check_vec) == 1):
            break
    return(i, check_vec)

print(start_of_marker(input_vec,4))
print(start_of_marker(input_vec,14))