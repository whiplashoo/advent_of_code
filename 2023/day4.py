from aoc import input_as_lines, parse_positive_ints_str

inp = input_as_lines("day4.txt")

total = 0
i = 1
for line in inp:
    line = line.split(": ")[1]
    line = line.split(" | ")
    w = set(parse_positive_ints_str(line[0]))
    p = set(parse_positive_ints_str(line[1]))
    u = set.intersection(w,p)
    if (len(u) > 0):
        total += 2 ** (len(u) - 1)
    i+=1

print(int(total))