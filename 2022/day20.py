from itertools import combinations

from aoc import input_as_lines, parse_ints_str

inp = input_as_lines("day19t.txt")

original = []

for line in inp:
    original.append(parse_ints_str(line)[0])

N = original[:]

print(len(set(original)), len(original))

i = 0
for n in original:
    print(f"Will move {n} in position {(i + n) % len(original)}")
    N.insert((i + n + 1) % len(original), n)
    del N[i]
    i += 1
    print(N)
