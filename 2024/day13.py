from aoc import input_as_lines, parse_positive_ints_str
import sys
from itertools import product

inp = input_as_lines("day13.txt")
combs = list(product(range(101), repeat = 2))

def solve(A, B, P):
    cost = sys.maxsize
    found = False
    bb = ((A[0] * P[1]) - (A[1] * P[0])) /  (A[0] * B[1]) - (A[1] * B[0]) 
    print(bb)

sum = 0
for i in range(0, len(inp), 4):
    A = parse_positive_ints_str(inp[i])
    B = parse_positive_ints_str(inp[i + 1])
    P = parse_positive_ints_str(inp[i + 2])
    sum += solve(A,B,P)
print(sum)

# a * 94 + b * 22 = 8400
# a * 34 + b * 67 = 5400
# a = (8400 - 22b) / 94
# a = (5400 - 67b) / 34
# (8400 - 22b) / 94 = (5400 - 67b) / 34
