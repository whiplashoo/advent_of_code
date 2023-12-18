from collections import defaultdict

from aoc import input_as_lines, print_dict_as_matrix

inp = input_as_lines("day18.txt")

moves = {
    "R": (1,0),
    "D": (0,1),
    "L": (-1,0),
    "U": (0,-1),
}
grid = defaultdict(lambda: ".")
cur = [0,0]
grid[(0,0)] = "#"

min_col = 2**10000
max_col = -2**10000
min_row = 2**10000
max_row = -2**10000

loop = set()
for line in inp:
    d, steps, color = line.replace("(", "").replace(")", "").split(" ")
    move = moves[d]
    for i in range(int(steps)):
        cur = [cur[0] + move[0], cur[1] + move[1]]
        grid[(cur[0], cur[1])] = "#"
        min_col = min(cur[0], min_col)
        max_col = max(cur[0], max_col)
        min_row = min(cur[1], min_row)
        max_row = max(cur[1], max_row)
        loop.add((cur[0], cur[1]))

def can_move(new_c, new_r):
    if new_r < min_row or new_c < min_col or new_r > max_row or new_c > max_col:
        return False
    if (new_c, new_r) in loop:
        return False
    return True

def bfs(N, start):
    queue = [(start)]
    visited = {start}
    loop.add(start)
    N[start] = "#"
    while queue:
        v = queue.pop(0)
        for move in moves.values():
            adj = (v[0] + move[0], v[1] + move[1])
            if adj not in visited and can_move(adj[0], adj[1]):
                visited.add(adj)
                queue.append(adj)
                loop.add(adj)
                N[adj] = "#"

bfs(grid, ((min_col + max_col) // 2, (min_row + max_row) // 2))
print_dict_as_matrix(grid)
print(len(loop))