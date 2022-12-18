from itertools import combinations

from aoc import input_as_lines, parse_ints_str

inp = input_as_lines("day18.txt")


def is_adjacent(a, b):
    same_dimensions = 0
    diff_one = False
    for i, j in zip(a, b):
        if i == j:
            same_dimensions += 1
        if abs(i-j) == 1:
            diff_one = True
    return same_dimensions == 2 and diff_one


area = {}
for line in inp:
    x, y, z = parse_ints_str(line)
    area[(x, y, z)] = 6

for a, b in combinations(area.keys(), 2):
    if is_adjacent(a, b):
        area[a] -= 1
        area[b] -= 1

ret = 0
for k in area:
    ret += area[k]

print(ret)
