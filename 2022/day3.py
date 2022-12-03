import string

from aoc import input_as_lines

inp = input_as_lines("day3.txt")


def get_priority(letter):
    pr = string.ascii_lowercase + string.ascii_uppercase
    return pr.index(letter) + 1


# PART 1
score = 0
for line in inp:
    first = line[0:len(line)//2]
    second = line[len(line)//2:len(line) + 1]
    for letter in first:
        if letter in second:
            score += get_priority(letter)
            break

print(score)

# PART 2
score = 0
for i in range(0, len(inp), 3):
    for letter in inp[i]:
        if letter in inp[i + 1] and letter in inp[i + 2]:
            score += get_priority(letter)
            break
print(score)
