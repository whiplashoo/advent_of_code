from aoc import input_as_lines, parse_positive_ints_str

inp = input_as_lines("day1.txt")
p1 = 0
p2 = 0

dial = 50

#PART 1
for line in inp:
    rot = parse_positive_ints_str(line)[0]
    d = line[0]
    for _ in range(rot):
        if d == "L":
            dial = (dial - 1 + 100) % 100
        else:
            dial = (dial + 1) % 100
        if dial == 0:
            p2 +=1
    print(dial)
    if dial == 0:
        p1 += 1

print(p1)

# PART 2
print(p2)
