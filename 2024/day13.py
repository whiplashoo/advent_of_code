from aoc import input_as_lines, parse_positive_ints_str
import sys
from itertools import product

inp = input_as_lines("day13.txt")
combs = list(product(range(101), repeat = 2))

def solve(A, B, P):
    cost = sys.maxsize
    found = False
    for aa, bb in combs:
        res_x = (A[0] * aa) + (B[0] * bb)
        res_y = (A[1] * aa) + (B[1] * bb)
        if res_x == P[0] and res_y == P[1]:
            cost = min((aa * 3) + bb, cost)
            found = True
    if found: 
        return cost 
    else:
        return 0

sum = 0
for i in range(0, len(inp), 4):
    A = parse_positive_ints_str(inp[i])
    B = parse_positive_ints_str(inp[i + 1])
    P = parse_positive_ints_str(inp[i + 2])
    sum += solve(A,B,P)
print(sum)


