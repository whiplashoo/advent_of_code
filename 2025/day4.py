from aoc import input_as_lines, print_matrix
from copy import deepcopy
inp = input_as_lines("day4.txt")

N = []
for line in inp:
    N.append([x for x in line])

ROWS = len(N)
COLS = len(N[0])
moves = [(-1, 0), (0, -1), (1, 0), (0, 1), (-1, -1), (-1, 1), (1,-1), (1, 1)]

p1 = 0
print_matrix(N)

for row in range(ROWS):
    for col in range(COLS):
        rolls = 0
        for move in moves:
            newR = row + move[0]
            newC = col + move[1]
            if newR >= 0 and newC >= 0 and newR < ROWS and newC < COLS:
                if N[newR][newC] == "@":
                    rolls += 1
        if N[row][col] == "@" and rolls < 4:
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
                    newR = row + move[0]
                    newC = col + move[1]
                    if newR >= 0 and newC >= 0 and newR < ROWS and newC < COLS:
                        if N[newR][newC] == "@":
                            rolls += 1
                if rolls < 4:
                    changes.append((row,col))
    if len(changes) == 0:
        break

print(p2)