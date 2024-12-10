from aoc import input_as_lines
inp = input_as_lines("day10.txt")

N = []
for line in inp:
    N.append([int(x) for x in line])

ROWS = len(N)
COLS = len(N[0])
moves = [(-1, 0), (0, -1), (1, 0), (0, 1)]

def can_move(matrix, new_r, new_c, cur_val):
    if (new_r < 0 or new_c < 0 or new_r >= ROWS or new_c >= COLS):
        return False
    if matrix[new_r][new_c] - cur_val == 1:
        return True
    return False

p1 = 0
p2 = 0

def bfs(N, start):
    global p1
    queue = [(p, 0) for p in start]
    visited = set(start)
    while queue:
        (v, steps) = queue.pop(0)
        cur_val = N[v[0]][v[1]]
        if steps == 9:
            p1 += len(queue) + 1
            return
        for move in moves:
            adj = (v[0] + move[0], v[1] + move[1])
            if adj not in visited and can_move(N, adj[0], adj[1], cur_val):
                visited.add(adj)
                queue.append((adj, steps + 1))
    return None

def bfs2(N, start):
    global p2
    queue = [(p, 0) for p in start]
    while queue:
        (v, steps) = queue.pop(0)
        cur_val = N[v[0]][v[1]]
        if steps == 9:
            p2 += len(queue) + 1
            return
        for move in moves:
            adj = (v[0] + move[0], v[1] + move[1])
            if can_move(N, adj[0], adj[1], cur_val):
                queue.append((adj, steps + 1))
    return None

for row in range(ROWS):
    for col in range(COLS):
        start = N[row][col]
        if start == 0:
            bfs(N, [(row, col)])
            bfs2(N, [(row, col)])

print(p1)
print(p2)
