from aoc import input_as_lines, parse_positive_ints_str

inp = input_as_lines("day1.txt")
p1 = 0

left = []
right = []

#PART 1
for line in inp:
    ints = parse_positive_ints_str(line)
    left.append(ints[0])
    right.append(ints[-1])

left.sort()
right.sort()

for i in range(0, len(left)):
    p1 += abs(left[i] - right[i])

print(p1)

# PART 2
p2 = 0

for i in range(0, len(left)):
    p2 += left[i] * right.count(left[i])

print(p2)