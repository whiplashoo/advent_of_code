from aoc import input_as_lines, print_matrix

inp = input_as_lines("day6.txt")

# row, col
moves = [(-1, 0),(0, 1), (1, 0), (0, -1)  ]
cur = 0

N = []
gx = gy = 0

for idx, line in enumerate(inp):
    N.append([h for h in line])
    if "^" in line:
        gx, gy = idx, line.index("^")

COLS = len(N[0])
ROWS = len(N)

N[gx][gy] = "."
visited = set()
visited.add((gx,gy))

while True:
    next_move = (gx + moves[cur][0], gy + moves[cur][1])
    if 0 <= next_move[0] < COLS and 0 <= next_move[1] < ROWS:
        next_cell = N[next_move[0]][next_move[1]]
        if N[next_move[0]][next_move[1]] == ".":
            gx, gy = next_move
            visited.add((next_move))
        else:
            cur = (cur + 1) % 4
    else:
        break
        
print(len(visited))



