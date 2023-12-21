from collections import defaultdict

from aoc import input_as_lines, print_dict_as_matrix

inp = input_as_lines("day21.txt")

graph = defaultdict(lambda: ".")
min_col = 2**10000
max_col = -2**10000
min_row = 2**10000
max_row = -2**10000
S = (0,0)
total_steps = 64
moves = [(-1, 0), (0, -1), (1, 0), (0, 1)]

for row, line in enumerate(inp):
    for col, x in enumerate(line):
        if x != ".":
            graph[(col, row)] = x
            if x == "S":
                S = (col, row)
            min_col = min(col, min_col)
            max_col = max(col, max_col)
            min_row = min(row, min_row)
            max_row = max(row, max_row)

final_plots = []

def can_move(N, adj):
    adj_val = N[adj]
    if adj_val == "#":
        return False
    return True

possible = {S}

for s in range(1, total_steps + 1):
    new_possible = set()
    for v in possible:
        for move in moves:
            adj = (v[0] + move[0], v[1] + move[1])
            if can_move(graph, adj):
                new_possible.add(adj)
    possible = new_possible
print(len(possible))
