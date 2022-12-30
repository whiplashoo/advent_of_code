from collections import defaultdict

from aoc import flatten, input_as_lines

inp = input_as_lines("day23.txt")


def get_rectangle_ground_tiles(grove):
    min_col = 2**10000
    max_col = -2**10000
    min_row = 2**10000
    max_row = -2**10000
    elves = 0
    for p in grove.keys():
        if grove[p] == "#":
            col, row = p
            min_col = min(col, min_col)
            max_col = max(col, max_col)
            min_row = min(row, min_row)
            max_row = max(row, max_row)
            elves += 1
    w = max_col - min_col + 1
    h = max_row - min_row + 1
    return (w * h) - elves


# col, row | x, y :
#           N,      NW,       NE       S,       SW,     SE
#           W,      NW,       SW       E,       NE,     SE
moves = [[(0, -1), (-1, -1), (1, -1)], [(0, 1), (-1, 1), (1, 1)],
         [(-1, 0), (-1, -1), (-1, 1)], [(1, 0), (1, -1), (1, 1)]]
moves_set = set(flatten(moves))
grove = defaultdict(lambda: ".")
for row, line in enumerate(inp):
    for col, letter in enumerate(line):
        if letter == "#":
            grove[(col, row)] = letter

rounds = 0
noone_moved = False
while not noone_moved:
    if rounds == 10:
        # Part 1 answer
        print(get_rectangle_ground_tiles(grove))
    proposals = defaultdict(lambda: [])
    elfs = [x for x in grove.keys() if grove[x] == "#"]
    noone_moved = True
    for elf in elfs:
        elf_col, elf_row = elf
        should_propose = False
        for move in moves_set:
            if grove[(elf_col + move[0], elf_row + move[1])] == "#":
                should_propose = True
        if should_propose:
            for direction in moves:
                will_propose_this = True
                for move in direction:
                    if grove[(elf_col + move[0], elf_row + move[1])] == "#":
                        will_propose_this = False
                        break
                if will_propose_this:
                    new_place = (
                        elf_col + direction[0][0], elf_row + direction[0][1])
                    proposals[new_place].append(elf)
                    break
    for new_place, old_places in proposals.items():
        if len(old_places) == 1:
            noone_moved = False
            grove[old_places[0]] = "."
            grove[new_place] = "#"
    moves.append(moves.pop(0))
    rounds += 1

# Part 2 answer
print(rounds)
