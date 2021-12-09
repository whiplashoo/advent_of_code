from aoc import input_as_lines, print_matrix

inp = input_as_lines("day9.txt")
N = []
for i in inp:
    N.append([int(x) for x in i])

moves = [(-1, 0), (0, -1), (1, 0), (0, 1)]

X = len(N[0])
Y = len(N)


def is_lower(y, x):
    point = N[y][x]
    for m in moves:
        move_y = y + m[0]
        move_x = x + m[1]
        if 0 <= move_y < Y and 0 <= move_x < X and point >= N[move_y][move_x]:
            return False
    return True


sum_low = 0
answers = []
for y in range(Y):
    for x in range(X):
        if is_lower(y, x):
            sum_low += 1 + N[y][x]
print(sum_low)
