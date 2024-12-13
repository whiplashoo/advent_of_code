from aoc import input_as_lines, parse_positive_ints_str
inp = input_as_lines("day13.txt")

def solve(A, B, P):
    P[1] += 10000000000000
    P[0] += 10000000000000
    bb = ((A[0] * P[1]) - (A[1] * P[0])) /  ((A[0] * B[1]) - (A[1] * B[0]))
    if bb > 0 and bb.is_integer():
        aa = (P[1] - B[1] * bb) / A[1]
        if aa.is_integer():
            return (aa * 3) + bb
    return 0

sum = 0
for i in range(0, len(inp), 4):
    A = parse_positive_ints_str(inp[i])
    B = parse_positive_ints_str(inp[i + 1])
    P = parse_positive_ints_str(inp[i + 2])
    sum += solve(A,B,P)
print(sum)