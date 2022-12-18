from collections import defaultdict
from copy import deepcopy

from aoc import input_as_string, print_matrix, print_matrix_reverse

jets = input_as_string("day17t.txt")

# For sample input:
# 20, 50, 100, 200
# 36, 78, 157, 308


def print_chamber(chamber_dict):
    """
    Helper to convert a dict chamber_dict to a grid and print it
    """
    max_y = -1000000
    for point in chamber_dict.keys():
        row, col = point
        max_y = max(row, max_y)
    COLS = 7
    ROWS = max_y + 2
    cave = [["." for col in range(COLS)] for row in range(ROWS)]
    for point in chamber_dict.keys():
        row, col = point
        cave[row][col] = chamber_dict[point]
    print_matrix_reverse(cave)
    print()
    print()


rocks = [
    ["####"],
    [".#.", "###", ".#."],
    ["..#", "..#", "###"],
    ["#", "#", "#", "#"],
    ["##", "##"]
]

chamber = defaultdict(lambda: ".")
for col in range(7):
    chamber[(0, col)] = "-"

top_row = 0

fallen_rocks = 0
cur_rock_idx = 0
cur_rock = rocks[cur_rock_idx]
jet_idx = 0
cur_jet = jets[jet_idx]


def get_rock_w(rock):
    return max([len(x) for x in rock])


def get_rock_h(rock):
    return len(rock)


def can_fall(rock, rock_w, next_row, rock_left):
    last_row = rock[-1]
    can_fall = True
    for col in range(rock_left, rock_left + rock_w):
        if last_row[col-rock_left] == "#" and next_row[col] == "#":
            can_fall = False
    return can_fall


def can_move_side(rock, rock_h, side_col, rock_bottom):
    last_col = [x[-1] for x in rock]
    can_move_side = True
    for row in range(rock_bottom, rock_bottom + rock_h):
        if last_col[row-rock_bottom] == "#" and side_col[row-rock_bottom] == "#":
            can_move_side = False
    return can_move_side


while fallen_rocks != 100:
    settled = False
    rock_w = get_rock_w(cur_rock)
    rock_h = get_rock_h(cur_rock)
    rock_left = 2
    rock_top = top_row + 3 + rock_h
    rock_bottom = rock_top - rock_h + 1
    # Rock appears at the top
    while not settled:
        # Jet push (check walls)
        if cur_jet == "<" and rock_left > 0:
            prev_col = [chamber[(rock_bottom + row, rock_left - 1)]
                        for row in range(rock_h)]
            if can_move_side(cur_rock, rock_h, prev_col, rock_bottom):
                rock_left -= 1
        elif cur_jet == ">" and rock_left + rock_w < 7:
            next_col = [chamber[(rock_bottom + row, rock_left + rock_w)]
                        for row in range(rock_h)]
            if can_move_side(cur_rock, rock_h, next_col, rock_bottom):
                rock_left += 1
        jet_idx += 1
        if jet_idx == len(jets):
            jet_idx = 0
        cur_jet = jets[jet_idx]
        # Rock falls one unit
        # If next row is floor or one of its cols
        # is the same as the rocks cols, settle.
        next_row = [chamber[(rock_bottom - 1, col)] for col in range(7)]
        print(
            f"fallen: {fallen_rocks} next row: {next_row}, rock_l: {rock_left}, rock_b: {rock_bottom}, cur_rock:{cur_rock_idx}")
        if rock_bottom - 1 != 0 and can_fall(cur_rock, rock_w, next_row, rock_left):
            rock_bottom -= 1
            rock_top -= 1
        else:
            for row in range(rock_h):
                for col in range(rock_w):
                    if cur_rock[row][col] == "#":
                        chamber[(rock_bottom + rock_h - row -
                                 1, col + rock_left)] = "#"
            cur_rock_idx += 1
            if cur_rock_idx == len(rocks):
                cur_rock_idx = 0
            cur_rock = rocks[cur_rock_idx]
            settled = True
            if rock_top > top_row:
                top_row = rock_top
            # print_chamber(chamber)
    fallen_rocks += 1

# print(chamber)
print(top_row)
