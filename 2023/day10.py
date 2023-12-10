from aoc import input_as_lines, print_matrix

inp = input_as_lines("day10.txt")

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
    

visited = set(get_start(N))
def bfs(N, start):
    queue = [(p, 0) for p in start]
    while queue:
        (v, steps) = queue.pop(0)
        cur_val = N[v[0]][v[1]]
        cant_move_count = 0
        for move in moves:
            adj = (v[0] + move[0], v[1] + move[1])
            if adj not in visited and can_move(N, adj[0], adj[1], cur_val, move):
                visited.add(adj)
                queue.append((adj, steps + 1))
            else:
                cant_move_count += 1
        if cant_move_count == 4:
            print("REACHED END: " + str(queue[0][1]))
            break


# PART 1
print(bfs(N, [get_start(N)]))
print(visited)