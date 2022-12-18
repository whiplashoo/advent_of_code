from collections import defaultdict
from itertools import cycle

from aoc import print_matrix_reverse
from PIL import Image

LEFT, RIGHT = "<", ">"
jetdir = {LEFT: -1, RIGHT: 1}

rocks = cycle((
    ((0, 0), (1, 0), (2, 0), (3, 0)),
    ((1, 0), (0, 1), (1, 1), (2, 1), (1, 2)),
    ((0, 0), (1, 0), (2, 0), (2, 1), (2, 2)),
    ((0, 0), (0, 1), (0, 2), (0, 3)),
    ((0, 0), (1, 0), (0, 1), (1, 1)),
))

with open("day17t.txt") as f:
    text = f.read().strip()
    jets = cycle(text)


def translatex(rock, dx):
    for idx in range(len(rock)):
        rock[idx][0] += dx


def translatey(rock, dy):
    for idx in range(len(rock)):
        rock[idx][1] += dy


def checkwalls(rock, dx):
    for p in rock:
        if not (0 <= p[0]+dx <= 6):
            return False
    return True


def checkblock(rock, G, dx, dy):
    for x, y in rock:
        if (x+dx, y+dy) in G:
            return False
    return True


def prune(G, top):
    for p in [p for p in G if p[1] < top - 100]:
        G.remove(p)


def print_chamber(chamber, rock_h, rock_w, cur_rock):
    max_y = -1000000
    for point in chamber:
        col, row = point
        max_y = max(row, max_y)
    COLS = 7
    ROWS = max_y + 2
    cave = [["." for col in range(COLS)] for row in range(ROWS + 4)]
    for row in range(len(cave)):
        for col in range(COLS):
            if (col, row) in chamber:
                cave[row][col] = "#"
    # for row in range(rock_h):
    #     for col in range(rock_w):
    #         if cur_rock[row][col] == "#":
    #             cave[rock_bottom + rock_h - row -
    #                  1][col + rock_left] = "@"
    #print_matrix_reverse(cave[len(cave) - 20: len(cave)])
    print()
    print()
    cave_top = cave[len(cave) - 20: len(cave)]
    ret = ""
    for row in cave_top[::-1]:
        ret += " ".join([str(x) for x in row])
        ret += "\n"
    return ret


G = set([(x, 0) for x in range(7)])
top = 0
idx = -1
part1 = None

with open("outp_true.txt", "w") as f:
    while True:
        idx += 1
        # rock falling procedure
        rock = [[x+2, y+top+4] for x, y in next(rocks)]
        while True:
            dir = jetdir[next(jets)]
            if checkwalls(rock, dir) and checkblock(rock, G, dir, 0):
                translatex(rock, dir)
            if not checkblock(rock, G, 0, -1):
                break
            translatey(rock, -1)
        G.update([(x, y) for x, y in rock])
        print(G)
        f.write(print_chamber(G, len(rock), max([len(x) for x in rock]), rock))
        top = max([p[1] for p in rock] + [top])
        f.write(f"Fallen: {idx + 1} top: {top}")
        f.write("\n")
        prune(G, top)

        # part 1
        if idx == 26:
            print("Answer 1:", top)
            break
