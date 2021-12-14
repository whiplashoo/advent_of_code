from aoc import input_as_lines
from collections import Counter
inp = input_as_lines("day12.txt")

cave = {}
for line in inp:
    r1 = line.split("-")[0]
    r2 = line.split("-")[1]
    if r1 not in cave.keys():
        cave[r1] = [r2]
    else:
        cave[r1].append(r2)
    if r2 not in cave.keys():
        cave[r2] = [r1]
    else:
        cave[r2].append(r1)


def dfs(cave, node, path):
    global counter
    path.append(node)
    if node == 'end':
        counter += 1
    else:
        for neighbour in cave[node]:
            if neighbour.isupper() or (neighbour.islower() and neighbour not in path):
                dfs(cave, neighbour, path[:])


def dfs2(cave, node, path):
    global counter
    path.append(node)
    if node == 'end':
        counter += 1
    else:
        for neighbour in cave[node]:
            if neighbour.isupper():
                dfs2(cave, neighbour, path[:])
            elif neighbour.islower() and neighbour != 'start':
                c = Counter(path)
                should_visit = True
                for k in c:
                    if k.islower() and c[k] == 2 and c[neighbour] == 1 and neighbour != k:
                        should_visit = False
                if should_visit and c[neighbour] < 2:
                    dfs2(cave, neighbour, path[:])


# PART 1
path = []
counter = 0
dfs(cave, 'start', path)
print(counter)
# PART 2
path = []
counter = 0
dfs2(cave, 'start', path)
print(counter)
