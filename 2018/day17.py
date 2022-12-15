from collections import defaultdict
from copy import deepcopy

from aoc import input_as_lines, parse_ints_str, print_matrix

inp = input_as_lines("day17t.txt")
veins = []

max_y = -1000

cave = defaultdict(lambda: ".")


def print_inf_cave(inf_cave, max_y):
    """
    Helper to convert a dict cave to a grid and print it
    """
    min_x = 1000
    max_x = -1000
    for point in inf_cave.keys():
        row, col = point
        min_x = min(col, min_x)
        max_x = max(col, max_x)
    COLS = max_x - min_x + 3
    ROWS = max_y + 2
    cave = [["." for col in range(COLS)] for row in range(ROWS)]
    for point in inf_cave.keys():
        row, col = point
        cave[row][col-min_x] = inf_cave[point]
    print("\n")
    print_matrix(cave)


for line in inp:
    vein = []
    line = line.split(", ")
    for p in line:
        if p.startswith("y="):
            ys = parse_ints_str(p)
            if len(ys) == 2:
                y0, y1 = ys[0], ys[1]
            else:
                y0 = y1 = ys[0]
            max_y = max(max_y, y1)
        else:
            xs = parse_ints_str(p)
            if len(xs) == 2:
                x0, x1 = xs[0], xs[1]
            else:
                x0 = x1 = xs[0]
    for yy in range(y0, y1 + 1):
        for xx in range(x0, x1 + 1):
            cave[(yy, xx)] = "#"

print_inf_cave(cave, max_y)
ROWS = max_y + 1


def solve1(cave):
    scol, srow = (500, 0)
    ret = 0
    overflowed = False
    while not overflowed:
        while True:
            ncol, nrow = scol, srow + 1
            if nrow >= ROWS:
                overflowed = True
                break
            if cave[(nrow, ncol)] == ".":
                srow = nrow
            elif cave[(nrow, ncol)] == "~" or cave[(nrow, ncol)] == "#":
                if cave[(nrow, ncol - 1)] == ".":
                    srow, scol = nrow, ncol - 1
                elif cave[(nrow, ncol + 1)] == ".":
                    srow, scol = nrow, ncol + 1
                else:
                    cave[(srow, scol)] = "~"
                    scol, srow = (500, 0)
                    ret += 1
                    break
    return ret


def solve2(cave):
    floor_y = max_y + 2
    scol, srow = (500, 0)
    ret = 0
    filled = False
    while not filled:
        while True:
            ncol, nrow = scol, srow + 1
            if nrow == 1 and cave[(nrow, ncol - 1)] == "~" and cave[(nrow, ncol + 1)] == "~" and cave[(nrow, ncol)] == "~":
                ret += 1
                filled = True
                break
            if nrow == floor_y:
                cave[(srow, scol)] = "~"
                scol, srow = (500, 0)
                ret += 1
                break
            elif cave[(nrow, ncol)] == ".":
                srow = nrow
            elif cave[(nrow, ncol)] == "~" or cave[(nrow, ncol)] == "#":
                if cave[(nrow, ncol - 1)] == ".":
                    srow, scol = nrow, ncol - 1
                elif cave[(nrow, ncol + 1)] == ".":
                    srow, scol = nrow, ncol + 1
                else:
                    cave[(srow, scol)] = "~"
                    scol, srow = (500, 0)
                    ret += 1
                    break

    return ret


# print(solve1(deepcopy(cave)))
# print(solve2(inf_cave))
