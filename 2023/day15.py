from aoc import input_as_string, print_matrix

inp = input_as_string("day15.txt").split(",")

s1 = 0
for a in inp:
    ss = 0
    for char in a:
        ss += ord(char)
        ss *= 17
        ss %= 256
    s1 += ss

print(s1)