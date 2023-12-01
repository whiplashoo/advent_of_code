import re

from aoc import input_as_lines, parse_positive_ints_str

inp = input_as_lines("day1.txt")
sum = 0

digits = ["one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]

# PART 1
for line in inp:
    ints = re.findall(r'[0-9]', line)
    first = ints[0]
    second = ints[-1]
    print(line + " " + str(int(str(first) + "" + str(second))))
    sum += int(ints[0] + ints[-1])
print(sum)

sum = 0
pos = {}
# PART 2

            
print(sum)