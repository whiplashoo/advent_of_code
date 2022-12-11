from aoc import input_as_lines

inp = input_as_lines("day10.txt")

X = 1
ticks = 0
ss = {}

for line in inp:
    line = line.split()
    if line[0] == "addx":
        ticks += 1
        ss[ticks] = X * ticks
        ticks += 1
        ss[ticks] = X * ticks
        X += int(line[1])
    else:
        ticks += 1
        ss[ticks] = X * ticks
print(ss)
ret = 0
for i in range(20, ticks + 1, 40):
    ret += ss[i]
print(f"ret: {ret}")
