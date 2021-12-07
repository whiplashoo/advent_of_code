from aoc import parse_ints_str

with open("day7.txt") as f:
    inp = parse_ints_str(f.read().rstrip("\n"))

sums1 = []

min_pos = min(inp)
max_pos = max(inp)
# PART 1
for pos in range(min_pos, max_pos + 1):
    sums1.append(sum([abs(pos - x) for x in inp]))
print(min(sums1))

# PART 2
sums2 = []
for pos in range(min_pos, max_pos + 1):
    sums2.append(sum([sum(range(abs(pos - x)+1)) for x in inp]))
print(min(sums2))
