from aoc import input_as_lines, print_matrix
inp = input_as_lines("day15.txt")

N = []
robot = None
seq = []
parse_moves = False

for i, line in enumerate(inp):
    if line == "":
        parse_moves = True
        continue
    if parse_moves:
        seq.extend([x for x in line])
    else: 
        row = []
        for j, x in enumerate(line):
            row.append(x)
            if x == "@":
                robot = [i,j]
        N.append(row)

ROWS = len(N)
COLS = len(N[0])
moves = {
    "^": (-1, 0),
    "<": (0, -1),
    "v": (1, 0),
    ">": (0, 1)
}

def can_move(matrix, new_r, new_c):
    if (new_r < 0 or new_c < 0 or new_r >= ROWS or new_c >= COLS):
        return False
    if matrix[new_r][new_c] == "#":
        return False
    return True

p1 = 0
p2 = 0

for m in seq:
    dx, dy = moves[m]
    rr = robot[0] + dx
    cc = robot[1] + dy
    print(f"Move {m} to rr {rr}, cc {cc}")
    if can_move(N, rr, cc):
        next = N[rr][cc]
        if next == ".":
            N[robot[0]][robot[1]] = "."
            N[robot[0] + dx][robot[1] + dy] = "@"
            robot[0] += dx
            robot[1] += dy
            continue
        while next == "O":
            if not can_move(N, rr + dx, cc + dy):
                break
            to_go = N[rr + dx][cc + dy]
            if to_go == ".":
                N[rr + dx][cc + dy] = "O"
                N[robot[0]][robot[1]] = "."
                N[robot[0] + dx][robot[1] + dy] = "@"
                robot[0] += dx
                robot[1] += dy
                break
            else:
                rr += dx
                cc += dy

def count_box(row,col):
    return 100 * row + col

for row, r in enumerate(N):
    for col, x in enumerate(r):
        if x == "O":
            p1 += count_box(row, col)
print(p1)

