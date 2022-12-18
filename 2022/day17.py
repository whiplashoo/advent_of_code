from collections import defaultdict
from copy import deepcopy

from aoc import input_as_string, print_matrix, print_matrix_reverse

jets = input_as_string("day17.txt")

# For sample input:
# 20, 50, 100, 200
# 36, 78, 157, 308


def print_chamber(chamber_dict, rock_h, rock_w, cur_rock):
    """
    Helper to convert a dict chamber_dict to a grid and print it
    """
    max_y = -1000000
    for point in chamber_dict.keys():
        row, col = point
        max_y = max(row, max_y)
    COLS = 7
    ROWS = max_y + 2
    cave = [["." for col in range(COLS)] for row in range(ROWS + 4)]
    for point in chamber_dict.keys():
        row, col = point
        cave[row][col] = chamber_dict[point]
    for row in range(rock_h):
        for col in range(rock_w):
            if cur_rock[row][col] == "#":
                cave[rock_bottom + rock_h - row -
                     1][col + rock_left] = "@"
    print_matrix_reverse(cave[len(cave) - 20: len(cave)])
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


def can_fall(rock, chamber, rock_left, rock_bottom):
    can_fall = True
    for row in range(get_rock_h(rock)):
        for col in range(get_rock_w(rock)):
            chamber_row = rock_bottom + rock_h - row - 1 - 1
            chamber_col = col + rock_left
            if cur_rock[row][col] == "#" and chamber[(chamber_row, chamber_col)] == "#":
                can_fall = False
                break
    return can_fall
    # for col in range(rock_left, rock_left + rock_w):
    #     if last_row[col-rock_left] == "#" and next_row[col] == "#":
    #         can_fall = False
    # return can_fall


def can_move_side(rock, chamber, rock_left, rock_bottom, dx):
    can_move_side = True
    for row in range(get_rock_h(rock)):
        for col in range(get_rock_w(rock)):
            chamber_row = rock_bottom + rock_h - row - 1
            chamber_col = col + rock_left + dx
            if cur_rock[row][col] == "#" and chamber[(chamber_row, chamber_col)] == "#":
                can_move_side = False
                break
    return can_move_side


# The error happens between 21 and 22
while fallen_rocks != 2022:
    settled = False
    rock_w = get_rock_w(cur_rock)
    rock_h = get_rock_h(cur_rock)
    rock_left = 2
    rock_top = top_row + 3 + rock_h
    rock_bottom = rock_top - rock_h + 1
    #print_chamber(chamber, rock_h, rock_w, cur_rock)
    # Rock appears at the top
    while not settled:
        # print_chamber(chamber, rock_h, rock_w, cur_rock)
        # print("will move: " + cur_jet + "\n")
        # Jet push (check walls)
        if cur_jet == "<" and rock_left > 0:
            if can_move_side(cur_rock, chamber, rock_left, rock_bottom, -1):
                rock_left -= 1
        elif cur_jet == ">" and rock_left + rock_w < 7:
            if can_move_side(cur_rock, chamber, rock_left, rock_bottom, 1):
                rock_left += 1
        jet_idx += 1
        if jet_idx == len(jets):
            jet_idx = 0
        cur_jet = jets[jet_idx]
        # Rock falls one unit
        # If next row is floor or one of its cols
        # is the same as the rocks cols, settle.
        next_row = [chamber[(rock_bottom - 1, col)] for col in range(7)]
        # print(
        # f"fallen: {fallen_rocks} next row: {next_row}, rock_l: {rock_left}, rock_b: {rock_bottom}, cur_rock:{cur_rock_idx}")
        if rock_bottom - 1 != 0 and can_fall(cur_rock, chamber, rock_left, rock_bottom):
            rock_bottom -= 1
            rock_top -= 1
        else:
            for row in range(rock_h):
                for col in range(rock_w):
                    if cur_rock[row][col] == "#":
                        chamber[(rock_bottom + rock_h - row -
                                 1, col + rock_left)] = "#"
            #print_chamber(chamber, rock_h, rock_w, cur_rock)
            cur_rock_idx += 1
            if cur_rock_idx == len(rocks):
                cur_rock_idx = 0
            cur_rock = rocks[cur_rock_idx]
            settled = True
            if rock_top > top_row:
                top_row = rock_top

    fallen_rocks += 1
    print(f"Fallen: {fallen_rocks} top row: {top_row}")


print(top_row)
