from aoc import input_as_lines, print_matrix

inp = input_as_lines("day10t.txt")

N = []
for line in inp:
    N.append([h for h in line])

moves = [(-1, 0), (0, -1), (1, 0), (0, 1)]
col = 0
row = 0
COLS = len(N[0])
ROWS = len(N)

valid_moves = {
    "|" : [(-1,0), (1,0)],
    "-": [(0,1), (0,-1)],
    "L": [(-1,0), (0,1)],
    "J": [(-1,0), (0,-1)],
    "7": [(1,0), (0,-1)],
    "F": [(1,0), (0,1)],
    "S": moves,
    ".": []
}

def get_start(N):
    for row in range(ROWS):
        for col in range(COLS):
            if N[row][col] == "S":
                return (row, col)
            
def can_move(N, new_r, new_c, cur_val, move):
    if (new_r < 0 or new_c < 0 or new_r >= len(N) or new_c >= len(N[0])):
        return False
    adj_val = N[new_r][new_c]
    if adj_val == "S" or adj_val == ".":
        return False
    if move in valid_moves[cur_val]:
         reverse_move = (-move[0], -move[1])
         if reverse_move in valid_moves[adj_val]:
            return True
    return False

loop = []
def bfs(N, start):
    queue = [(p, 0) for p in start]
    visited = set(start)
    while queue:
        (v, steps) = queue.pop(0)
        cur_val = N[v[0]][v[1]]
        cant_move_count = 0
        loop.append(v)
        for move in moves:
            adj = (v[0] + move[0], v[1] + move[1])
            if adj not in visited and can_move(N, adj[0], adj[1], cur_val, move):
                visited.add(adj)
                queue.append((adj, steps + 1))
            else:
                cant_move_count += 1
        if cant_move_count == 4:
            print("REACHED END: " + str(queue[0][1]))
            loop.append(queue.pop(0)[0])
            break
bfs(N, [get_start(N)])

# PART 2
NN = []
for line in inp:
    rr = []
    for h in line:
        rr.append(h)
        rr.append("#")
    NN.append(rr)
    NN.append(["#" for _ in  range(len(line * 2))])

col = 0
row = 0
COLS = len(NN[0])
ROWS = len(NN)
loop = [(x * 2, y * 2) for (x,y) in loop]

to_add = []
for row in range(ROWS):
    for col in range(COLS):
        if (row,col) in loop:
            for m in valid_moves[NN[row][col]]:
                link = "-" if m[0] == 0 else "|"
                NN[row + m[0]][col + m[1]] = link
                to_add.append((row + m[0], col + m[1]))

for i in to_add:
    loop.append(i)
print_matrix(NN)

def can_fill(N, new_r, new_c):
    if (new_r < 0 or new_c < 0 or new_r >= len(N) or new_c >= len(N[0])):
        return False
    if (new_r, new_c) in loop:
        return False
    return True

def flood_fill(N, start):
    queue = [(p, 0) for p in start]
    visited = set(start)
    while queue:
        (v, steps) = queue.pop(0)
        for move in moves:
            adj = (v[0] + move[0], v[1] + move[1])
            if adj not in visited and can_fill(N, adj[0], adj[1]):
                visited.add(adj)
                queue.append((adj, steps + 1))
                N[adj[0]][adj[1]] = "%"
        # print_matrix(NN)
        # print()
flood_fill(NN, [get_start(NN)])
print()
print_matrix(NN)

s = 0
for row in range(ROWS):
    for col in range(COLS):
        if NN[row][col] != "#" and (row, col) not in loop:
            s += 1
print(s)