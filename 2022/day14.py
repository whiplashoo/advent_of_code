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

min_y = 0
COLS = max_x - min_x + 1
ROWS = max_y + 1
cave = [["." for col in range(COLS)] for row in range(ROWS)]

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
                cave[yy][xx] = "#"

# PART 1
scol, srow = (500 - min_x, 0)
ret = 0
reached_abyss = False
while not reached_abyss:
    while True:
        ncol, nrow = scol, srow + 1
        if nrow >= ROWS:
            reached_abyss = True
            break
        if cave[nrow][ncol] == ".":
            srow = nrow
        elif cave[nrow][ncol] == "o" or cave[nrow][ncol] == "#":
            if cave[nrow][ncol - 1] == ".":
                srow, scol = nrow, ncol - 1
            elif cave[nrow][ncol + 1] == ".":
                srow, scol = nrow, ncol + 1
            else:
                cave[srow][scol] = "o"
                scol, srow = (500 - min_x, 0)
                ret += 1
                break


print(ret)
