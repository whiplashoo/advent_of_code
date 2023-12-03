from collections import defaultdict
from math import prod

from aoc import input_as_lines

inp = input_as_lines("day3t.txt")
matrix = []

all_nums = []

def get_all_ints(line):
    i = 0
    ints = []
    while i < len(line):
        if line[i].isdigit():
            num = line[i]
            i += 1
            while line[i].isdigit():
                num += line[i]
                i += 1
            ints.append(int(num))
        i += 1
    return ints


for row, line in enumerate(inp):
    i = 0
    while i < len(line):
        if line[i].isdigit():
            num = line[i]
            positions = [[row, i]]
            i += 1
            while i < len(line) and line[i].isdigit():
                num += line[i]
                positions.append([row, i])
                i += 1
            int_num = int(num)
            all_nums.append((int(num), positions))
        i += 1
    matrix.append([h for h in line])

moves = [(-1, 0), (0, -1), (1, 0), (0, 1), (-1,-1), (1,1), (1, -1), (-1, 1)]
COLS = len(matrix[0])
ROWS = len(matrix)
found = []
gears = defaultdict(list)
p2_sum = 0
for num, ps in all_nums:
    added = False
    has_gear = False
    for p in ps:
        if added:
            break
        for move in moves:
             rr = p[0] + move[0]
             cc = p[1] + move[1]
             if rr >= ROWS or cc >= COLS or rr < 0 or cc < 0:
                 continue
             a = matrix[rr][cc]
             if not a.isdigit() and a != ".":
                found.append(num)
                added = True
                if a == "*":
                    gears[(rr,cc)].append(num)
                    if len(gears[(rr, cc)]) == 2:
                        p2_sum += prod(gears[(rr, cc)])


print(sum(found))
print(p2_sum)
