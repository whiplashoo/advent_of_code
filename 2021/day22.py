from aoc import input_as_lines, parse_ints_str
from itertools import product
inp = input_as_lines("day22.txt")

on = set()
p2 = True
for step in inp:
    split = step.split(" ")
    turn = split[0]
    c = parse_ints_str(split[1])
    in_bounds = True
    if not p2:
        for i in c:
            if i < -50 or i > 50:
                in_bounds = False
                break
    if in_bounds:
        cubes = [set(range(c[0], c[1] + 1)), set(range(c[2], c[3] + 1)),
                 set(range(c[4], c[5] + 1))]
        prod = set(product(*cubes))
        if turn == "on":
            on = on.union(prod)
        else:
            on = on.difference(prod)

print(len(on))
