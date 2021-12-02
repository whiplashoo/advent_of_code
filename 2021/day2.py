from aoc import input_as_lines

course = input_as_lines("day2.txt")

# PART 1
horiz_pos = 0
depth = 0
for inst in course:
    split = inst.split(" ")
    if split[0] == "forward":
        horiz_pos += int(split[1])
    elif split[0] == "down":
        depth += int(split[1])
    else:
        depth -= int(split[1])

print(horiz_pos * depth)

# PART 2
horiz_pos = 0
depth = 0
aim = 0
for inst in course:
    split = inst.split(" ")
    val = int(split[1])
    if split[0] == "forward":
        horiz_pos += val
        depth += aim * val
    elif split[0] == "down":
        aim += val
    else:
        aim -= val

print(horiz_pos * depth)
