
from aoc import input_as_lines, parse_positive_ints_str

inp = input_as_lines("day4.txt")


# PART 1
ret = 0
for line in inp:
    pairs = parse_positive_ints_str(line)
    x0 = pairs[0]
    x1 = pairs[1]
    y0 = pairs[2]
    y1 = pairs[3]
    if (x0 <= y0 and x1 >= y1) or (y0 <= x0 and y1 >= x1):
        ret += 1
print(ret)

# PART 2
ret = 0
for line in inp:
    pairs = parse_positive_ints_str(line)
    x0 = pairs[0]
    x1 = pairs[1]
    y0 = pairs[2]
    y1 = pairs[3]
    one = set(range(x0, x1 + 1))
    two = set(range(y0, y1 + 1))
    if len(one & two) != 0:
        ret += 1
print(ret)
