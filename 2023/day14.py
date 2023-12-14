from aoc import input_as_lines, print_matrix

inp = input_as_lines("day14.txt")
N = []

for line in inp:
    N.append([r for r in line])

print_matrix(N)
ROWS = len(N)
COLS = len(N[0])

top_blocks = [0] * COLS

for row in range(ROWS):
    for col in range(COLS):
        cell = N[row][col]
        if cell == "#":
            top_blocks[col] = row + 1
        if cell == "O":
            top_blocks[col] += 1
            N[row][col] = "."
            N[top_blocks[col] - 1][col] = "O"

print_matrix(N)

s1 = 0
for row in range(ROWS):
    val = ROWS - row
    s1 += val * N[row].count("O")
print(s1)