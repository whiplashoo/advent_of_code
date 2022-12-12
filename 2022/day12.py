import string
from collections import deque

from aoc import input_as_lines, print_matrix

# I hate pathfinding...
inp = input_as_lines("day12.txt")
matrix = []
for line in inp:
    matrix.append([h for h in line])

moves = [(-1, 0), (0, -1), (1, 0), (0, 1)]
col = 0
row = 0
COLS = len(matrix[0])
ROWS = len(matrix)

char_dict = {c: i for i, c in enumerate(string.ascii_lowercase)}


def get_start(matrix):
    for row in range(ROWS):
        for col in range(COLS):
            if matrix[row][col] == "S":
                return (row, col)


def get_start2(matrix):
    a = []
    for row in range(ROWS):
        for col in range(COLS):
            if matrix[row][col] in ["S", "a"]:
                a.append((row, col))
    return a


def can_move(matrix, new_r, new_c, cur_val):
    if (new_r < 0 or new_c < 0 or new_r >= len(matrix) or new_c >= len(matrix[0])):
        return False
    if cur_val == "S":
        cur_val = "a"
    adj_val = matrix[new_r][new_c]
    if adj_val == "S":
        return False
    if adj_val == "E":
        adj_val = "z"
    return char_dict[adj_val] <= char_dict[cur_val] + 1


def bfs(matrix, start):
    queue = [(p, 0) for p in start]
    visited = set(start)
    while queue:
        (v, steps) = queue.pop(0)
        cur_val = matrix[v[0]][v[1]]
        if cur_val == "E":
            print("FOUND! " + str(steps))
            return
        for move in moves:
            adj = (v[0] + move[0], v[1] + move[1])
            if adj not in visited and can_move(matrix, adj[0], adj[1], cur_val):
                visited.add(adj)
                queue.append((adj, steps + 1))
    return None


# PART 1
print(bfs(matrix, [get_start(matrix)]))
# PART 2
print(bfs(matrix, get_start2(matrix)))
