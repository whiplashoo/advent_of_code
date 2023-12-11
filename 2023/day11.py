import itertools
from copy import deepcopy

from aoc import get_manhattan_distance, input_as_lines

inp = input_as_lines("day11.txt")

galaxies = []
for row, line in enumerate(inp):
    for col, c in enumerate(line):
        if c == "#":
            galaxies.append([row,col])

all_rows = set([g[0] for g in galaxies])
all_cols = set([g[1] for g in galaxies])
empty_rows = sorted(set(range(row)).difference(all_rows))
empty_cols = sorted(set(range(col)).difference(all_cols))

ex_galaxies = deepcopy(galaxies)
for i, g in enumerate(galaxies):
    for r in empty_rows:
        if g[0] > r:
            ex_galaxies[i][0] += 999999 # 1 if we are on part 1
    for c in empty_cols:
        if g[1] > c:
            ex_galaxies[i][1] += 999999 # 1 if we are on part 2

combos = list(itertools.combinations(ex_galaxies, 2))
s = 0
for c in combos:
    s += get_manhattan_distance(c[0], c[1])

print(s)