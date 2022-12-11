from aoc import input_as_lines, print_matrix

inp = input_as_lines("day10.txt")

X = 1
ticks = 0
ss = {}
xv = {}
# Part 1
for line in inp:
    line = line.split()
    if line[0] == "addx":
        ticks += 1
        ss[ticks] = X * ticks
        xv[ticks] = X
        ticks += 1
        ss[ticks] = X * ticks
        xv[ticks] = X
        X += int(line[1])
    else:
        ticks += 1
        ss[ticks] = X * ticks
        xv[ticks] = X
print(ss)
print(xv)
ret = 0
for i in range(20, ticks + 1, 40):
    ret += ss[i]
print(f"ret: {ret}")

# PART 2
crt = [["." for _ in range(40)] for y in range(6)]
for t in range(1, ticks):
    row = t // 40
    col = (t-1) % 40
    sprite_col = [(xv[t] % 40) - 1, (xv[t] % 40), (xv[t] % 40) + 1]
    if col in sprite_col:
        crt[row][col] = "#"

print_matrix(crt)
