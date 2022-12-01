cals = []

count = 0

with open("2022day1input.txt","r") as f:
    for line in f:
        if line.rstrip() == "":
            cals.append(count)
            count = 0
        else:
            count += int(line.rstrip())

print(max(cals))

cals.sort()
print(sum(cals[-3:]))
