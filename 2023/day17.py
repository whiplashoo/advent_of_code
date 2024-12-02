import heapq
from collections import defaultdict, deque

from aoc import input_as_lines, print_matrix

inp = input_as_lines("day17t.txt")

N = []
for line in inp:
    N.append([int(i) for i in line])
print_matrix(N)

graph = defaultdict(list)

ROWS = len(N)
COLS = len(N[0])

costs = []
for row in range(ROWS):
    for col in range(COLS):
        for rr in range(-3,4):
            new_r = row + rr
            if new_r > 0 and new_r < ROWS and new_r != row:
                graph[(col,row)].append((col, new_r))
        for cc in range(-3,4):
            new_c = col + cc
            if new_c > 0 and new_c < COLS and new_c != col:
                graph[(col,row)].append((new_c, row))
                
print(graph)


def a_star(grid, start, goal):
    def heuristic(a,b):
        return abs(a[0] - b[0]) + abs(a[1] - b[1])
    frontier = []
    heapq.heappush(frontier, (start, grid[start]))
    came_from = dict()
    cost_so_far = dict()
    came_from[start] = None
    cost_so_far[start] = grid[start]

    while frontier:
         current = heapq.heappop(frontier)[1]
         if current == goal:
             print("REACHED GOAL")
             print(came_from)
             return
         for next in graph[current]:
             pass
             #new_cost = cost_so_far[current] + 
             
