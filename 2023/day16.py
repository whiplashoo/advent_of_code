from collections import defaultdict
from copy import deepcopy

from aoc import input_as_lines, print_dict_as_matrix

inp = input_as_lines("day16.txt")
cave = defaultdict()

for row, line in enumerate(inp):
    for col, c in enumerate(line):
        cave[(col, row)] = c

ROWS = len(inp)
COLS = len(inp[0])
print(ROWS, COLS)

# N, E, S, W
dirs = [ (0, -1), (1, 0), (0, 1), (-1, 0) ]

angles = {
    ".": {
        (0, -1): [0],
        (0, 1): [0],
        (-1, 0): [0],
        (1, 0): [0],
    },
    "|": {
        (0, -1): [0],
        (0, 1): [0],
        (-1, 0): [-1, 1],
        (1, 0): [-1, 1],
    },
    "-": {
        (0, -1): [-1, 1],
        (0, 1): [-1, 1],
        (-1, 0): [0],
        (1, 0): [0],
    }, 
    "/": {
        (0, -1): [1],
        (0, 1): [1],
        (-1, 0): [-1],
        (1, 0): [-1],
    }, 
    "\\": {
        (0, -1): [-1],
        (0, 1): [-1],
        (-1, 0): [1],
        (1, 0): [1],
    }, 

}

cur = (0,0)
beams = [[(-1,0), (1, 0)]]
energized = []

def hash_beam(beam, next_cell):
    return f"{beam[0][0]}_{beam[0][1]}_{beam[1][0]}_{beam[1][1]}_{next_cell[0]}_{next_cell[1]}"

seen = []
i = 0
while len(beams) > 0:
    new_beams = []
    finished_beams = []
    for beam in beams:
        cur_dir = beam[1]
        next_col = beam[0][0] + cur_dir[0]
        next_row = beam[0][1] + cur_dir[1]
        next_cell = (next_col, next_row) 
        if next_col < 0 or next_col >= COLS or next_row < 0 or next_row >= ROWS:
            finished_beams.append(beam)
            continue
        if hash_beam(beam, next_cell) in seen:
            finished_beams.append(beam)
            continue
        seen.append(hash_beam(beam, next_cell))
        dir_changes = angles[cave[next_cell]][cur_dir]
        beam[0] = next_cell
        beam[1] = dirs[(dirs.index(cur_dir) + dir_changes[0]) % len(dirs)]
        if len(dir_changes) == 2:
            new_beam = []
            new_beam.append(next_cell)
            new_beam.append(dirs[(dirs.index(cur_dir) + dir_changes[1]) % len(dirs)])
            new_beams.append(new_beam)
        if next_cell not in energized:
            energized.append(next_cell)
    beams += new_beams
    for b in finished_beams:
        beams.remove(b)
    i += 1

print(energized)
print(len(energized))