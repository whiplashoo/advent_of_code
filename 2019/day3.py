from aoc import input_as_lines

inp = input_as_lines("day3.txt")
wire1, wire2 = inp[0].split(","), inp[1].split(",")
d = {"U": (0, 1), "D": (0, -1), "L": (-1, 0), "R": (1, 0)}


def get_points(wire):
    points = []
    x = y = 0
    for w in wire:
        direction = w[0]
        val = int(w[1:])
        for _ in range(val):
            x += d[direction][0]
            y += d[direction][1]
            points.append((x, y))
    return points


points1 = get_points(wire1)
points2 = get_points(wire2)

cross = set(points1).intersection(points2)
manh = [abs(a[0]) + abs(a[1]) for a in cross]
print(min(manh))
