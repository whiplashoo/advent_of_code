from aoc import input_as_lines
import re

inp = input_as_lines("day5.txt")

vents = []
max_x = 0
max_y = 0
for line in inp:
    r = [int(x) for x in re.findall('[0-9]+', line)]
    vents.append([(r[0], r[1]), (r[2], r[3])])
    max_x = max(max_x, r[0], r[2])
    max_y = max(max_y, r[1], r[3])

d = [[0 for col in range(max_x + 1)] for row in range(max_y + 1)]

overlaps = 0
for v in vents:
    x1 = v[0][0]
    x2 = v[1][0]
    y1 = v[0][1]
    y2 = v[1][1]
    # horizontal: x1 = x2
    if x1 == x2:
        x = x1
        # if y1 < y2
        if y1 < y2:
            for i in range(y1, y2 + 1):
                d[i][x] += 1
        # if y1 > y2
        if y1 > y2:
            for i in range(y2, y1 + 1):
                d[i][x] += 1
    # vertical: y1 = y2
    elif y1 == y2:
        y = y1
        # if x1 < x2
        if x1 < x2:
            for i in range(x1, x2 + 1):
                d[y][i] += 1
        # if x1 > x2
        if x1 > x2:
            for i in range(x2, x1 + 1):
                d[y][i] += 1
    # diagonal: abs(y1 - y2) == abs(x1 - x2)
    elif abs(y1 - y2) == abs(x1 - x2):
        # e.g. (1,1) -> (3,3)
        if x1 < x2 and y1 < y2:
            diff = x2 - x1
            for i in range(diff + 1):
                d[y1 + i][x1 + i] += 1
        # e.g. (3,3) -> (1,1)
        if x1 > x2 and y1 > y2:
            diff = x1 - x2
            for i in range(diff + 1):
                d[y2 + i][x2 + i] += 1
        # e.g. (7,9) -> (9,7)
        if x1 < x2 and y1 > y2:
            diff = x2 - x1
            for i in range(diff + 1):
                d[y1 - i][x1 + i] += 1
        # e.g. (9,7) -> (7,9)
        if x1 > x2 and y1 < y2:
            diff = x1 - x2
            for i in range(diff + 1):
                d[y1 + i][x1 - i] += 1

for i in range(len(d)):
    for j in range(len(d[0])):
        if d[i][j] >= 2:
            overlaps += 1
print(overlaps)
