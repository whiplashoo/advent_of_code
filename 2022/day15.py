import sys
from collections import defaultdict

from aoc import (get_manhattan_distance, input_as_lines, parse_ints_str,
                 print_matrix)

inp = input_as_lines("day15.txt")
target_row = 2000000

area = defaultdict(lambda: ".")


def print_inf_area(inf_area):
    """
    Helper to convert a dict area to a grid and print it
    """
    max_x = max_y = -sys.maxsize
    min_x = min_y = sys.maxsize
    for point in inf_area.keys():
        col, row = point
        min_x = min(col, min_x)
        max_x = max(col, max_x)
        min_y = min(row, min_y)
        max_y = max(row, max_y)
    COLS = max_x - min_x + 1
    ROWS = max_y - min_y + 1
    area_matrix = [["." for col in range(COLS)] for row in range(ROWS)]
    for point in inf_area.keys():
        col, row = point
        area_matrix[row - min_y][col-min_x] = inf_area[point]
    print("\n")
    start_y = min_y
    for row in area_matrix:
        row.insert(0, start_y)
        start_y += 1
    area_matrix.insert(0, [i for i in range(min_x, max_x+1)])
    print_matrix(area_matrix)


# PART 1
xs = set()
for line in inp:
    scol, srow, bcol, brow = parse_ints_str(line)
    sensor = (scol, srow)
    beacon = (bcol, brow)
    area[sensor] = "S"
    area[beacon] = "B"
    manh_dist = get_manhattan_distance(sensor, beacon)
    vertical_dist = abs(srow - target_row)  # 3

    if vertical_dist <= manh_dist:
        draw_on_side = manh_dist - vertical_dist
        for col in range(scol - draw_on_side, scol + draw_on_side):
            xs.add(col)
    # Add to the area dict only when debugging
    # if area[(col, target_row)] == ".":
    #     area[(col, target_row)] = "#"
# print(len(xs))

# PART 2 (WIP)
area = defaultdict(lambda: ".")
xs = set()
ys = set()
ys_map = defaultdict(lambda: [])
for line in inp:
    scol, srow, bcol, brow = parse_ints_str(line)
    sensor = (scol, srow)
    beacon = (bcol, brow)
    area[sensor] = "S"
    area[beacon] = "B"
    manh_dist = get_manhattan_distance(sensor, beacon)
    draw_on_side = manh_dist
    for row in range(srow, srow - manh_dist - 2, -1):
        min_x = scol - draw_on_side
        max_x = scol + draw_on_side + 1
        if ys_map[row] == []:
            ys_map[row] = [(4000000, 0)]
        y_row = ys_map[row]  # this is a list
        for min_max in y_row:
            min_max[0] = min(min_x, min_max[0])
            min_max[1] = max(max_x, min_max[1])
        draw_on_side -= 1
    draw_on_side = manh_dist
    for row in range(srow + 1, srow + manh_dist + 2):
        draw_on_side -= 1
        for col in range(scol - draw_on_side, scol + draw_on_side + 1):
            xs.add(col)
            ys.add(row)
# print_inf_area(area)

limit = 4000000
