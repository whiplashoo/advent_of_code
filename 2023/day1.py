import re

from aoc import input_as_lines, parse_positive_ints_str

inp = input_as_lines("day1.txt")
sum = 0

digits = ["one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]

#PART 1
for line in inp:
    ints = re.findall(r'[0-9]', line)
    first = ints[0]
    second = ints[-1]
    print(line + " " + str(int(str(first) + "" + str(second))))
    sum += int(ints[0] + ints[-1])
print(sum)

sum = 0
pos = {}

first_int = ""
last_int = ""
# PART 2
for line in inp:
    first_idx = 5000
    last_idx = -1
    for d in digits:
        f_occ = line.find(d)
        if f_occ != -1:
            if f_occ < first_idx:
                first_idx = f_occ
                first_int = d
        l_occ = line.rfind(d)
        if l_occ != -1:
            if l_occ > last_idx:
                last_idx = l_occ
                last_int = d
    for d in range(10):
        d = str(d)
        f_occ = line.find(d)
        if f_occ != -1:
            if f_occ < first_idx:
                first_idx = f_occ
                first_int = str(d)
        l_occ = line.rfind(d)
        if l_occ != -1:
            if l_occ > last_idx:
                last_idx = l_occ
                last_int = str(d)
    print(first_idx, last_idx)
    print(first_int, last_int)
    if len(first_int) > 1:
        first_int = str(digits.index(first_int) + 1)
    if len(last_int) > 1:
        last_int = str(digits.index(last_int) + 1)
    sum += int(first_int + last_int)
    print("------------------")
            
print(sum)