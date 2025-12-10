from aoc import input_as_lines, print_matrix

inp = input_as_lines("day7.txt")

p1 = 0
N = []
for line in inp:
	N.append([c for c in line])

ROWS = len(N)
COLS = len(N[0])
beams = [(0, inp[0].index("S"))]

for r in range(ROWS - 1):
	for c in range(COLS):
		a = N[r][c]
		if (r,c) in beams and N[r+1][c] == "^":
			p1 += 1
			if c + 1 < COLS:
				beams.append((r + 1, c + 1))
			if c - 1 >= 0:
				beams.append((r + 1, c - 1))
		elif (r,c) in beams and N[r+1][c] == ".":
			beams.append((r + 1, c))

print(p1)