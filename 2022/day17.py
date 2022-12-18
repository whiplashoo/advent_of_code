from collections import defaultdict

from aoc import input_as_string, print_matrix_reverse

jets = input_as_string("day17.txt")


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
                cave[rock_bot + rock_h - row -
                     1][col + rock_x] = "@"
    print_matrix_reverse(cave[len(cave) - 20: len(cave)])
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


def get_rock_w(rock):
    return max([len(x) for x in rock])


def get_rock_h(rock):
    return len(rock)


def can_fall(rock, chamber, rock_x, rock_bot):
    can_fall = True
    for row in range(get_rock_h(rock)):
        for col in range(get_rock_w(rock)):
            chamber_row = rock_bot + rock_h - row - 1 - 1
            chamber_col = col + rock_x
            if cur_rock[row][col] == "#" and chamber[(chamber_row, chamber_col)] == "#":
                can_fall = False
                break
    return can_fall


def can_move_side(rock, chamber, rock_x, rock_bot, dx):
    can_move_side = True
    for row in range(get_rock_h(rock)):
        for col in range(get_rock_w(rock)):
            chamber_row = rock_bot + rock_h - row - 1
            chamber_col = col + rock_x + dx
            if cur_rock[row][col] == "#" and chamber[(chamber_row, chamber_col)] == "#":
                can_move_side = False
                break
    return can_move_side


top_row = 0
fallen_rocks = 0
jet_idx = 0

while fallen_rocks != 2022:
    cur_rock = rocks[fallen_rocks % 5]
    settled = False
    rock_w = get_rock_w(cur_rock)
    rock_h = get_rock_h(cur_rock)
    rock_x = 2
    rock_bot = top_row + 3
    while not settled:
        # Jet push (check walls)
        cur_jet = jets[jet_idx % len(jets)]
        if cur_jet == "<" and rock_x > 0:
            if can_move_side(cur_rock, chamber, rock_x, rock_bot, -1):
                rock_x -= 1
        elif cur_jet == ">" and rock_x + rock_w < 7:
            if can_move_side(cur_rock, chamber, rock_x, rock_bot, 1):
                rock_x += 1
        jet_idx += 1
        # Rock falls one unit
        if rock_bot - 1 != 0 and can_fall(cur_rock, chamber, rock_x, rock_bot):
            rock_bot -= 1
        else:
            for row in range(rock_h):
                for col in range(rock_w):
                    if cur_rock[row][col] == "#":
                        chamber[(rock_bot + rock_h - row -
                                 1, col + rock_x)] = "#"
            settled = True
            top_row = max(top_row, rock_bot + rock_h)

    fallen_rocks += 1

print(top_row)
