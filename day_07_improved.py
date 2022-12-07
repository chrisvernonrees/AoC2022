def dict_update(dict, open_vec, value):
    for i in range(len(open_vec)):
        dict[open_vec[i]] = dict[open_vec[i]] + value
    return(dict)

def direct_write(list):
    direct = ''
    for i in range(len(list)):
        direct += list[i] + '/'
    return(direct)

direct_dict = {}
open_vec = []

with open("2022day7input.txt", "r") as f:
    for line in f:
        if '$ cd ' in line:
            if '..' not in line:
                dir = line.rstrip().replace('$ cd ','')
                open_vec.append(dir)
                dir_string = direct_write(open_vec)
                direct_dict[dir_string] = 0
            else:
                open_vec = open_vec[:-1]
                dir_string = direct_write(open_vec)
        elif ('$ ls' in line) or ('dir ' in line):
            pass
        else:
            size, name = (line.rstrip()).split()
            folders = []
            for i in range(len(open_vec)):
                    folders.append(direct_write(open_vec[:i+1]))
            direct_dict = dict_update(direct_dict,folders,int(size))

count = 0
for key in direct_dict:
    if direct_dict[key] <= 100000:
        count += direct_dict[key]
print(count)

filtered_dict = {}
disk_space, free_space = 70000000, 30000000
space_needed = free_space - (disk_space - direct_dict['//'])

for key in direct_dict:
    if ((direct_dict[key]-space_needed) >= 0):
        filtered_dict[key] = direct_dict[key]

min_dir = min(filtered_dict, key=filtered_dict.get)
print(min_dir, filtered_dict[min_dir])

