import re

from aoc import input_as_lines, parse_positive_ints_str

inp = input_as_lines("day2.txt")
sum = 0

cubes = {
    "red": 0,
    "green": 0,
    "blue": 0,
}

id = 1
#PART 1
for line in inp:
    line = line.split(": ")[1]
    line = list(reversed(line.replace(",","").replace(";","").split(" ")))
    i = 0
    while i < len(line):
        cubes[line[i]] += int(line[i+1])
        i += 2
    print(cubes)
    if cubes["red"] <=12 and cubes["green"] <=13 and cubes["blue"] <= 14:
        sum += id
    id += 1
    cubes = {
        "red": 0,
        "green": 0,
        "blue": 0,
    }

print(sum)