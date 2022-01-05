from aoc import input_as_lines, parse_ints_str
from itertools import product
inp = input_as_lines("day22m.txt")

on = set()
# for step in inp:
#     split = step.split(" ")
#     turn = split[0]
#     c = parse_ints_str(split[1])
#     in_bounds = True
#     for i in c:
#         if i < -50 or i > 50:
#             in_bounds = False
#             break
#     if in_bounds:
#         cubes = [set(range(c[0], c[1] + 1)), set(range(c[2], c[3] + 1)),
#                  set(range(c[4], c[5] + 1))]
#         prod = set(product(*cubes))
#         if turn == "on":
#             on = on.union(prod)
#         else:
#             on = on.difference(prod)
x = [50, -50]
y = [50, -50]
z = [50, -50]
for step in inp:
    split = step.split(" ")
    turn = split[0]
    c = parse_ints_str(split[1])

    in_bounds = True
    for i in c:
        if i < -50 or i > 50:
            in_bounds = False
            break
    if in_bounds:
        if turn == "on":
            if c[0] < x[0]:
                x[0] = c[0]
            if c[1] > x[1]:
                x[1] = c[1]
            if c[2] < y[0]:
                y[0] = c[2]
            if c[3] > y[1]:
                y[1] = c[3]
            if c[4] < z[0]:
                z[0] = c[4]
            if c[5] > z[1]:
                z[1] = c[5]
        else:
            if c[1] > x[0]:
                x[0] = c[1]
            if c[0] < x[1] and c[0] > x[0]:
                x[1] = c[0]
            if c[3] > y[0]:
                y[0] = c[3]
            if c[2] < y[1] and c[2] > y[0]:
                y[1] = c[2]
            if c[5] > z[0]:
                z[0] = c[5]
            if c[4] < z[1] and c[4] > z[0]:
                z[1] = c[4]
    print(x, y, z)
cubes = [set(range(x[0], x[1] + 1)), set(range(y[0], y[1] + 1)),
         set(range(z[0], z[1] + 1))]
prod = set(product(*cubes))
print(prod)
print(len(prod))
