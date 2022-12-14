
from functools import cmp_to_key

from aoc import input_as_lines

inp = input_as_lines("day13.txt")

inp.append("")

# Eval to the rescue!


def parse_packet(line):
    p = eval(line)
    return p


def compare(left, right):
    n = max(len(left), len(right))
    for i in range(n):
        if i >= len(left):
            return True  # change to 1 for Part 2
        if i >= len(right):
            return False  # change to -1 for Part 2
        left_val = left[i]
        right_val = right[i]
        if isinstance(left_val, int) and isinstance(right_val, int):
            if left_val < right_val:
                return True  # change to 1 for Part 2
            if left_val > right_val:
                return False  # change to -1 for Part 2
        else:
            if isinstance(left_val, int):
                left_val = [left_val]
            if isinstance(right_val, int):
                right_val = [right_val]
            c = compare(left_val, right_val)
            if c is not None:
                return c


# PART 1
packets = []
ret = 0
idx = 1
for line in inp:
    if line == "":
        if compare(packets[0], packets[1]):
            ret += idx
        packets = []
        idx += 1
        continue
    packets.append(parse_packet(line))
print(ret)

# PART 2
packets = [[[2]], [[6]]]
for line in inp:
    if line == "":
        continue
    packets.append(parse_packet(line))

packets.sort(key=cmp_to_key(compare), reverse=True)
print((packets.index([[2]]) + 1) * (packets.index([[6]]) + 1))
