from itertools import permutations

from aoc import input_as_lines, parse_ints_str, print_matrix

inp = input_as_lines("day16t.txt")

valves = {}
rates = {}

for line in inp:
    v = line[6:8]
    rates[v] = parse_ints_str(line)[0]
    if "valves " in line:
        valves[v] = line.split("valves ")[1].split(", ")
    else:
        valves[v] = line.split("valve ")[1]

print(valves)
print(rates)
perms = permutations(valves.keys(), len(valves.keys()))
paths = []
for p in perms:
    if p[0] == "AA":
        paths.append(p)
pressures = {}
for p in paths:
    ticks = 30
    current_pressure = 0
    new_pressure = 0
    idx = 0
    while ticks != 0:
        current_pressure += new_pressure
        new_pressure = 0
        curr_valve = p[idx]
        if rates[curr_valve] != 0:
            new_pressure = rates[curr_valve]
        idx += 1
        ticks -= 1
        if idx == len(p):
            current_pressure += current_pressure * ticks
            break
    pressures[current_pressure] = p

for pr in pressures:
    print(pr, pressures[pr])
