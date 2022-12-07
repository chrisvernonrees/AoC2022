def dict_update(dict,open_vec,value):
    for i in range(len(open_vec)):
        dict[open_vec[i]] = dict[open_vec[i]] + value
    return(dict)

direct_dict = {}
open_vec = []
count = 1

with open("2022day7input.txt","r") as f:
    for line in f:
        if '$ cd ' in line:
            if '..' not in line:
                direct_dict[count] = 0
                open_vec.append(count)
                count += 1
            else:
                open_vec = open_vec[:-1]
        elif ('$ ls' in line) or ('dir ' in line):
            pass
        else:
            size, name = (line.rstrip()).split()
            direct_dict = dict_update(direct_dict,open_vec,int(size))

count = 0
for key in direct_dict:
    if direct_dict[key] <= 100000:
        count += direct_dict[key]
print(count)

filtered_dict = {}
disk_space, free_space = 70000000, 30000000
space_needed = free_space - (disk_space - direct_dict[1])

for key in direct_dict:
    if ((direct_dict[key]-space_needed) >= 0):
        filtered_dict[key] = direct_dict[key]

min_dir = min(filtered_dict, key=filtered_dict.get)
print(min_dir, filtered_dict[min_dir])
