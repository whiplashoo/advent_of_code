from aoc import input_as_lines

inp = input_as_lines("day1.txt")
cals = []

# PART 1
bucket = 0
for i in inp:
    if i == "":
        cals.append(bucket)
        bucket = 0
    else:
        bucket += int(i.rstrip('\n'))
print(max(cals))

# PART 2
print(sum(sorted(cals, reverse=True)[:3]))
