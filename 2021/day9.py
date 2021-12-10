from aoc import input_as_lines, print_matrix
from collections import deque as queue

inp = input_as_lines("day9.txt")
N = []
for i in inp:
    N.append([int(x) for x in i])

moves = [(-1, 0), (0, -1), (1, 0), (0, 1)]


def is_lower(y, x):
    point = N[y][x]
    for m in moves:
        move_y = y + m[0]
        move_x = x + m[1]
        if 0 <= move_y < Y and 0 <= move_x < X and point >= N[move_y][move_x]:
            return False
    return True


def bfs(matrix, visited, y, x):
    q = queue()
    basin_sum = 1
    q.append((y, x))
    visited[y][x] = True
    while len(q) > 0:
        y, x = q.popleft()
        for m in moves:
            move_y = y + m[0]
            move_x = x + m[1]
            if 0 <= move_y < Y and 0 <= move_x < X and not visited[move_y][move_x] and matrix[move_y][move_x] != 9:
                q.append((move_y, move_x))
                visited[move_y][move_x] = True
                basin_sum += 1
    return basin_sum


# PART 1
X = len(N[0])
Y = len(N)
sum_low = 0
for y in range(Y):
    for x in range(X):
        if is_lower(y, x):
            sum_low += 1 + N[y][x]
print(sum_low)

# PART 2
basins = []
visited = [[False for col in range(X)] for row in range(Y)]
for y in range(Y):
    for x in range(X):
        if is_lower(y, x):
            basins.append(bfs(N, visited, y, x))

s_basins = sorted(basins)
print(s_basins[-1] * s_basins[-2] * s_basins[-3])
