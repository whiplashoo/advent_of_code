import sys

from aoc import input_as_lines, print_matrix

inp = input_as_lines("day22.txt")


def print_map(map, me_row, me_col, cur_move):
    """
    Helper to convert a dict area to a grid and print it
    """
    max_x = max_y = -sys.maxsize
    for point in map.keys():
        row, col = point
        max_x = max(col, max_x)
        max_y = max(row, max_y)
    COLS = max_x + 1
    ROWS = max_y + 1
    area_matrix = [[" " for col in range(COLS)] for row in range(ROWS)]
    for point in map.keys():
        row, col = point
        area_matrix[row][col] = map[point]
    area_matrix[me_row][me_col] = facings[cur_move]
    print_matrix(area_matrix)


def get_first_col(N, row):
    m = [k[1] for k in N.keys() if k[0] == row]
    return min(m)


def get_last_col(N, row):
    m = [k[1] for k in N.keys() if k[0] == row]
    return max(m)


def get_first_row(N, col):
    m = [k[0] for k in N.keys() if k[1] == col]
    return min(m)


def get_last_row(N, col):
    m = [k[0] for k in N.keys() if k[1] == col]
    return max(m)


N = {}


for row, line in enumerate(inp):
    if line == "":
        continue
    if "." in line:
        for col, tile in enumerate(line):
            if tile != " ":
                N[(row, col)] = tile
    else:
        inst = line

path = []
cur = 0
token = ""
while cur < len(inst):
    if inst[cur] in ["L", "R"]:
        path.append(int(token))
        path.append(inst[cur])
        token = ""
    else:
        token += inst[cur]
    cur += 1
path.append(int(token))
print(path)

# row, col
moves = [(0, 1), (1, 0),  (0, -1), (-1, 0)]
facings = [">", "⬇", "<", "⬆"]

cur_move = 0
cur_row = 0
cur_col = get_first_col(N, 0)
#print_map(N, cur_row, cur_col, cur_move)
for p in path:
    print(p)
    if p == "R":
        cur_move = (cur_move + 1) % 4
    elif p == "L":
        cur_move = (cur_move - 1) % 4
    else:
        move = moves[cur_move]
        for i in range(p):
            move_row = cur_row + move[0]
            move_col = cur_col + move[1]
            if move_row > get_last_row(N, cur_col):
                move_row = get_first_row(N, cur_col)
            if move_row < get_first_row(N, cur_col):
                move_row = get_last_row(N, cur_col)
            if move_col > get_last_col(N, cur_row):
                move_col = get_first_col(N, cur_row)
            if move_col < get_first_col(N, cur_row):
                move_col = get_last_col(N, cur_row)
            if N[move_row, move_col] == "#":
                break
            cur_col = move_col
            cur_row = move_row
    # print()
    # print()
   #print_map(N, cur_row, cur_col, cur_move)

print((1000 * (cur_row + 1) + 4 * (cur_col + 1) + cur_move))
