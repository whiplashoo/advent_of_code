
from aoc import input_as_lines

inp = input_as_lines("day13.txt")

inp.append("")


def parse_packet(line):
    print(line)
    p = eval(line)
    return p


def compare(left, right):
    n = max(len(left), len(right))
    for i in range(n):
        if i >= len(left):
            return True
        if i >= len(right):
            return False
        left_val = left[i]
        right_val = right[i]
        if isinstance(left_val, int) and isinstance(right_val, int):
            if left_val < right_val:
                return True
            if left_val > right_val:
                return False
        else:
            if isinstance(left_val, int):
                left_val = [left_val]
            if isinstance(right_val, int):
                right_val = [right_val]
            c = compare(left_val, right_val)
            if c is not None:
                return c


packets = []
ret = 0
idx = 1
for line in inp:
    if line == "":
        if compare(packets[0], packets[1]):
            print(str(idx) + "IS OK")
            ret += idx
        packets = []
        idx += 1
        continue
    print("------------------")
    packets.append(parse_packet(line))
print(ret)
