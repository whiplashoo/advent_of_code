from aoc import input_as_lines, print_matrix

inp = input_as_lines("day13.txt")
N = []

def scan_rows(N):
    ROWS = len(N)
    for row in range(ROWS - 1):
        cur_row = N[row]
        next_row = N[row + 1]
        if cur_row == next_row:
            top, bot = row, row + 1
            while True:
                if (top == 0 or bot == ROWS -1) and N[top] == N[bot]:
                    return (row + 1) * 100
                if N[top] != N[bot]:
                    break
                else:
                    top -=1
                    bot +=1
    return 0

def get_col(N, col):
    return [x[col] for x in N]

def scan_cols(N):
    COLS = len(N[0])
    for col in range(COLS - 1):
        cur_col = get_col(N, col)
        next_col = get_col(N, col+1)
        if cur_col == next_col:
            left, right = col, col + 1
            while True:
                if (left == 0 or right == COLS -1) and get_col(N, left) == get_col(N, right):
                    return col + 1
                if get_col(N, left) != get_col(N, right):
                    break
                else:
                    left -= 1
                    right += 1
    return 0

s = 0
for line in inp:
    if line == "":
        rs = scan_rows(N)
        cs = scan_cols(N)
        s += rs + cs
        N = []
    else:
        N.append([h for h in line])

s += scan_rows(N) + scan_cols(N)
print(s)


