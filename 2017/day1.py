from aoc import input_as_string

inp = input_as_string("day1.txt")

# PART 1
s = 0
for i in range(len(inp)):
    if inp[i] == inp[i-1]:
        s += int(inp[i])
print(s)

# PART 2
s = 0
step = len(inp) // 2
for i in range(len(inp)):
    if inp[i] == inp[i - step]:
        s += int(inp[i])
print(s)
