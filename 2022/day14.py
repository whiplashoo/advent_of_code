from collections import defaultdict
from copy import deepcopy

from aoc import input_as_lines, print_matrix

inp = input_as_lines("day14.txt")
paths = []

min_x = 1000
max_x = -1000
max_y = -1000
for line in inp:
    path = []
    line = [x.split(",") for x in line.split(" -> ")]
    for p in line:
        x = int(p[0])
        y = int(p[1])
        min_x = min(min_x, x)
        max_x = max(max_x, x)
        max_y = max(max_y, y)
        path.append((int(p[0]), int(p[1])))
    paths.append(path)

COLS = max_x - min_x + 1
ROWS = max_y + 1
inf_cave = defaultdict(lambda: ".")

for path in paths:
    for i in range(len(path) - 1):
        cx, cy = path[i+1]
        px, py = path[i]
        cx -= min_x
        px -= min_x
        startx = min(cx, px)
        endx = max(cx, px)
        starty = min(cy, py)
        endy = max(cy, py)
        for yy in range(starty, endy + 1):
            for xx in range(startx, endx + 1):
                inf_cave[(yy, xx)] = "#"


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


def solve1(cave):
    scol, srow = (500 - min_x, 0)
    ret = 0
    reached_abyss = False
    while not reached_abyss:
        while True:
            ncol, nrow = scol, srow + 1
            if nrow >= ROWS:
                reached_abyss = True
                break
            if cave[(nrow, ncol)] == ".":
                srow = nrow
            elif cave[(nrow, ncol)] == "o" or cave[(nrow, ncol)] == "#":
                if cave[(nrow, ncol - 1)] == ".":
                    srow, scol = nrow, ncol - 1
                elif cave[(nrow, ncol + 1)] == ".":
                    srow, scol = nrow, ncol + 1
                else:
                    cave[(srow, scol)] = "o"
                    scol, srow = (500 - min_x, 0)
                    ret += 1
                    break
    return ret


def solve2(cave):
    floor_y = max_y + 2
    scol, srow = (500 - min_x, 0)
    ret = 0
    filled = False
    while not filled:
        while True:
            ncol, nrow = scol, srow + 1
            if nrow == 1 and cave[(nrow, ncol - 1)] == "o" and cave[(nrow, ncol + 1)] == "o" and cave[(nrow, ncol)] == "o":
                ret += 1
                filled = True
                break
            if nrow == floor_y:
                cave[(srow, scol)] = "o"
                scol, srow = (500 - min_x, 0)
                ret += 1
                break
            elif cave[(nrow, ncol)] == ".":
                srow = nrow
            elif cave[(nrow, ncol)] == "o" or cave[(nrow, ncol)] == "#":
                if cave[(nrow, ncol - 1)] == ".":
                    srow, scol = nrow, ncol - 1
                elif cave[(nrow, ncol + 1)] == ".":
                    srow, scol = nrow, ncol + 1
                else:
                    cave[(srow, scol)] = "o"
                    scol, srow = (500 - min_x, 0)
                    ret += 1
                    break

    return ret


print(solve1(deepcopy(inf_cave)))
print(solve2(inf_cave))
