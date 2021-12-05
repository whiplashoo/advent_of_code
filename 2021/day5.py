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

d = [[0 for col in range(max_x + 2)] for row in range(max_y + 2)]

print(max_x, max_y)
overlaps = 0
for v in vents:
    x1 = v[0][0]
    x2 = v[1][0]
    y1 = v[0][1]
    y2 = v[1][1]

    dx = x2 - x1
    dy = y2 - y1

    if dx > 0:
        dx = 1
    elif dx < 0:
        dx = -1
    if dy > 0:
        dy = 1
    elif dy < 0:
        dy = -1

    x, y = v[0]
    while (x, y) != v[1]:
        print(x, y)
        d[x][y] += 1
        x += dx
        y += dy
    d[x2][y2] += 1

for i in range(len(d)):
    for j in range(len(d[0])):
        if d[i][j] >= 2:
            overlaps += 1
print(overlaps)
