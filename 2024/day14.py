from aoc import input_as_lines, parse_ints_str, print_matrix
inp = input_as_lines("day14.txt")

robots = []
vs = []
for line in inp:
    line = parse_ints_str(line)
    robot = [line[0], line[1]]
    robots.append(robot)
    vs.append((line[2], line[3]))

ROWS = 103
COLS = 101

def can_move(matrix, new_r, new_c, cur_val):
    if (new_r < 0 or new_c < 0 or new_r >= ROWS or new_c >= COLS):
        return False
    if matrix[new_r][new_c] - cur_val == 1:
        return True
    return False

def create_matrix(rows, cols):
    return [[" " for _ in range(cols)] for _ in range(rows)]

N = create_matrix(ROWS, COLS)

for i in range(200):
    for n, robot in enumerate(robots):
        N[robot[1]][robot[0]] = " "
        next_col = (robot[0] + vs[n][0]) % COLS
        next_row = (robot[1] + vs[n][1]) % ROWS
        robot[0] = next_col
        robot[1] = next_row
        N[next_row][next_col] = "*"
    print("--------------------")
    print(i)
    print("--------------------")
    print_matrix(N)


q1 = q2 = q3 = q4 = 0
for col, row in robots:
    if row < ROWS // 2 and col < COLS // 2:
        q1 += 1
    elif row < ROWS // 2 and col > COLS // 2:
        q2 += 1
    elif row > ROWS // 2 and col < COLS // 2:
        q3 += 1
    elif row > ROWS // 2 and col > COLS // 2:
        q4 += 1

print(q1*q2*q3*q4)