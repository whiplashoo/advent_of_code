from aoc import input_as_string, parse_positive_ints_str
import re

inp = input_as_string("day3.txt")

#PART 1
p1 = 0
regex1 = r"mul\(\d+,\d+\)"
matches1 = re.finditer(regex1, inp, re.MULTILINE)

for match in matches1:
    ints = parse_positive_ints_str(match.group())
    p1 += ints[0] * ints[1]

print(p1)

#PART 2
p2 = 0
regex2 = r"mul\(\d+,\d+\)|do\(\)|don't\(\)"
matches2 = re.finditer(regex2, inp, re.MULTILINE)
enabled = True

for matchNum, match in enumerate(matches2, start=1):
    m = match.group()
    if enabled and "mul" in m:
        ints = parse_positive_ints_str(m)
        p2 += ints[0] * ints[1]
    elif "do()" in m:
        enabled = True
    elif "don't()" in m:
        enabled = False

print(p2)