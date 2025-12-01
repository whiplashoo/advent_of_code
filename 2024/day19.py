from aoc import input_as_lines, print_matrix
inp = input_as_lines("day19t.txt")
import itertools

parse_designs = False

towels = []
designs = []
max_len = 0
for idx, line in enumerate(inp):
    if idx == 1: continue
    if idx == 0:
        towels = line.split(", ")
    else:
        designs.append(line)
        max_len = max(max_len, len(line))

print(towels)
print(designs)
print(max_len)
p1 = 0

for design in designs:
    found = False
    for i in range(len(design)):
        if found: break
        combs = itertools.product(towels, repeat= i+1)
        for c in combs:
            str_c = "".join(c)
            print(str_c)
            if str_c == design:
                p1 += 1
                found = True
                break

print(p1)