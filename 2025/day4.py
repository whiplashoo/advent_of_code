from aoc import input_as_lines
inp = input_as_lines("day4.txt")

N = []
for line in inp:
    N.append([x for x in line])

ROWS = len(N)
COLS = len(N[0])
moves = [(-1, 0), (0, -1), (1, 0), (0, 1), (-1, -1), (-1, 1), (1,-1), (1, 1)]

p1 = 0

for row in range(ROWS):
    for col in range(COLS):
        if N[row][col] == "@":
            rolls = 0
            for move in moves:
                rr = row + move[0]
                cc = col + move[1]
                if rr >= 0 and cc >= 0 and rr < ROWS and cc < COLS:
                    if N[rr][cc] == "@":
                        rolls += 1
            if rolls < 4:
                p1 += 1

print(p1)

p2 = 0
changes = []

while True:
    p2 += len(changes)
    for change in changes:
        N[change[0]][change[1]] = "." 
    changes = []
    for row in range(ROWS):
        for col in range(COLS):
            if N[row][col] == "@": 
                rolls = 0
                for move in moves:
                    rr = row + move[0]
                    cc = col + move[1]
                    if rr >= 0 and cc >= 0 and rr < ROWS and cc < COLS:
                        if N[rr][cc] == "@":
                            rolls += 1
                if rolls < 4:
                    changes.append((row,col))
    if len(changes) == 0:
        break

print(p2)