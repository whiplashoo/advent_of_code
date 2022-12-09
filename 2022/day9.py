from aoc import input_as_lines, print_matrix

inp = input_as_lines("day9.txt")

moves = {"L": (-1, 0), "D": (0, -1), "R": (1, 0), "U": (0, 1)}

hx = hy = 0
tx = ty = 0
visited = {(0, 0)}

# PART 1
for line in inp:
    dir = line.split()[0]
    steps = int(line.split()[1])
    move = moves[dir]
    for step in range(steps):
        hx += move[0]
        hy += move[1]
        if hx - tx == 2 and hy == ty:
            tx += 1
        elif hx - tx == -2 and hy == ty:
            tx -= 1
        elif hy - ty == 2 and hx == tx:
            ty += 1
        elif hy - ty == -2 and hx == tx:
            ty -= 1
        elif hx - tx == 2 and hy != ty:
            ty = hy
            tx += 1
        elif hx - tx == -2 and hy != ty:
            ty = hy
            tx -= 1
        elif hy - ty == 2 and hx != tx:
            tx = hx
            ty += 1
        elif hy - ty == -2 and hx != tx:
            tx = hx
            ty -= 1
        visited.add((tx, ty))

print(len(visited))

# PART 2
# NOT GOING TO CLEAN THIS UP!
hx = hy = 0
visited = {(0, 0)}
knots = [[0, 0] for _ in range(10)]
for line in inp:
    dir = line.split()[0]
    steps = int(line.split()[1])
    move = moves[dir]
    for step in range(steps):
        knots[0][0] += move[0]
        knots[0][1] += move[1]
        hx = knots[0][0]
        hy = knots[0][1]
        for i in range(1, 10):
            nx = knots[i][0]
            ny = knots[i][1]
            if hx - knots[i][0] == 2 and hy == knots[i][1]:
                knots[i][0] += 1
            elif hx - knots[i][0] == -2 and hy == knots[i][1]:
                knots[i][0] -= 1
            elif hy - knots[i][1] == 2 and hx == knots[i][0]:
                knots[i][1] += 1
            elif hy - knots[i][1] == -2 and hx == knots[i][0]:
                knots[i][1] -= 1
            elif hx - knots[i][0] == 2 and hy != knots[i][1]:
                if abs(hy - knots[i][1]) == 1:
                    knots[i][1] = hy
                else:
                    knots[i][1] += 1 if hy > knots[i][1] else -1
                knots[i][0] += 1
            elif hx - knots[i][0] == -2 and hy != knots[i][1]:
                if abs(hy - knots[i][1]) == 1:
                    knots[i][1] = hy
                else:
                    knots[i][1] += 1 if hy > knots[i][1] else -1
                knots[i][0] -= 1
            elif hy - knots[i][1] == 2 and hx != knots[i][0]:
                if abs(hx - knots[i][0]) == 1:
                    knots[i][0] = hx
                else:
                    knots[i][0] += 1 if hx > knots[i][0] else -1
                knots[i][1] += 1
            elif hy - knots[i][1] == -2 and hx != knots[i][0]:
                if abs(hx - knots[i][0]) == 1:
                    knots[i][0] = hx
                else:
                    knots[i][0] += 1 if hx > knots[i][0] else -1
                knots[i][1] -= 1
            hx = knots[i][0]
            hy = knots[i][1]
            if i == 9:
                visited.add((hx, hy))

print(len(visited))
