from aoc import input_as_lines

inp = input_as_lines("day4.txt")

moves = [(-1, 0), (0, -1), (1, 0), (0, 1), (-1, -1), (1, -1), (-1, 1), (1, 1)]

N = []
for line in inp:
    N.append([h for h in line])

COLS = len(N[0])
ROWS = len(N)
p1 = 0

def can_move(new_c, new_r):
    return new_r >= 0 and new_c >= 0 and new_r < ROWS and new_c < COLS

for row in range(ROWS):
    for col in range(COLS):
        cur = N[row][col]
        if cur == "X":
            for move in moves:
                xr = row
                xc = col
                word = "X"
                for i in range(3):
                    xc += move[0]
                    xr += move[1] 
                    if can_move(xc, xr):
                        word += N[xr][xc]
                        if word == "XMAS":
                            p1 += 1 
                            break

print(p1)

p2 = 0

def is_in_bounds(r, c):
    return 0 <= r < ROWS and 0 <= c < COLS

diag1 = [(-1, -1), (1, 1)]
diag2 = [(1, -1), (-1, 1)]

for row in range(ROWS):
    for col in range(COLS):
        cur = N[row][col]
        if cur == "A": 
            valid_xmas = True
            for d1, d2 in [(diag1, diag2)]:
                try:
                    d1_0_r, d1_0_c = row + d1[0][0], col + d1[0][1]  
                    d1_1_r, d1_1_c = row + d1[1][0], col + d1[1][1]  
                    d2_0_r, d2_0_c = row + d2[0][0], col + d2[0][1]  
                    d2_1_r, d2_1_c = row + d2[1][0], col + d2[1][1]  

                    if not (is_in_bounds(d1_0_r, d1_0_c) and is_in_bounds(d1_1_r, d1_1_c) and
                            is_in_bounds(d2_0_r, d2_0_c) and is_in_bounds(d2_1_r, d2_1_c)):
                        valid_xmas = False
                        break

                    d1_0 = N[d1_0_r][d1_0_c]
                    d1_1 = N[d1_1_r][d1_1_c]
                    d2_0 = N[d2_0_r][d2_0_c]
                    d2_1 = N[d2_1_r][d2_1_c]

                    if not (
                        (d1_0 + d1_1 in ["MS", "SM"]) and
                        (d2_0 + d2_1 in ["MS", "SM"])
                    ):
                        valid_xmas = False
                        break

                except IndexError:
                    valid_xmas = False
                    break

            if valid_xmas:
                p2 += 1

print(p2)
