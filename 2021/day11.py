from aoc import input_as_lines, print_matrix

inp = input_as_lines("day11.txt")

steps = 0
flashes = 0

N = []
for i in inp:
    N.append([int(x) for x in i])
X = len(N[0])
Y = len(N)

moves = [(-1, 0), (0, -1), (1, 0), (0, 1), (-1, -1), (1, -1), (-1, 1), (1, 1)]


def flash(row, col, has_flashed):
    global flashes
    flashes += 1
    has_flashed[row][col] = True
    for m in moves:
        rr = row + m[0]
        cc = col + m[1]
        if 0 <= rr < Y and 0 <= cc < X:
            N[rr][cc] += 1
            if not has_flashed[rr][cc] and N[rr][cc] >= 10:
                flash(rr, cc, has_flashed)


# PART 1: while steps < 100:
# PART 2
while True:
    has_flashed = [[False for col in range(X)] for row in range(Y)]
    for row in range(Y):
        for col in range(X):
            N[row][col] += 1
            if not has_flashed[row][col] and N[row][col] >= 10:
                flash(row, col, has_flashed)
    currently_flashing = 0
    for row in range(Y):
        for col in range(X):
            if N[row][col] > 9:
                N[row][col] = 0
                currently_flashing += 1
    steps += 1
    if currently_flashing == X*Y:
        print(steps)
        break

print(flashes)
