from aoc import input_as_lines, print_matrix

inp = input_as_lines("day13t.txt")
moves = [(-1, 0), (0, -1), (1, 0), (0, 1)]
N = []
s_rows = 0

def scan_rows(N):
    for row in range(ROWS - 1):
        cur_row = N[row]
        next_row = N[row + 1]
        if cur_row == next_row:
            top, bot = row, row + 1
            print(f"SAME: {row, row+1}")
            while top >=0 and bot < ROWS:
                top -= 1
                bot += 1
                if N[top] != N[bot]:
                    break

for line in inp:
    if line == "":
        COLS = len(N[0])
        ROWS = len(N)
        scan_rows(N)
        N = []
    N.append([h for h in line])





