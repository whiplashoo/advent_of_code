import re

directions = ['E', 'S', 'W', 'N']


def move(direction, x, y, val):
    if direction == 'N':
        y += val
    elif direction == 'S':
        y -= val
    elif direction == 'W':
        x -= val
    elif direction == 'E':
        x += val
    return x, y


def part_one(instructions):
    x = 0
    y = 0
    facing = 'E'
    for inst in instructions:
        cmd = inst[0]
        val = int(re.findall(r'\d+', inst)[0])
        if cmd in directions:
            x, y = move(cmd, x, y, val)
        if cmd == 'F':
            x, y = move(facing, x, y, val)
        elif cmd == 'R':
            current_dir = directions.index(facing)
            val /= 90
            facing = directions[int((current_dir + val) % 4)]
        elif cmd == 'L':
            current_dir = directions.index(facing)
            val /= 90
            facing = directions[int((current_dir - val) % 4)]

    distance = abs(x) + abs(y)
    return distance


def part_two(instructions):
    x = 0
    y = 0
    wx = 10
    wy = 1
    for inst in instructions:
        cmd = inst[0]
        val = int(re.findall(r'\d+', inst)[0])
        if cmd in directions:
            wx, wy = move(cmd, wx, wy, val)
        if cmd == 'F':
            for i in range(val):
                x += wx
                y += wy
        elif cmd == 'R':
            val /= 90
            for i in range(int(val)):
                wx, wy = wy, -wx
        elif cmd == 'L':
            val /= 90
            for i in range(int(val)):
                wx, wy = -wy, wx
    distance = abs(x) + abs(y)
    return distance


with open("day12.txt") as f:
    instructions = []
    for line in f:
        instructions.append(line.strip())
    print(part_one(instructions))
    print(part_two(instructions))
