from collections import defaultdict

from aoc import input_as_lines, parse_positive_ints_str

inp = input_as_lines("day5.txt")

seeds = []

i = 0
while i < len(inp):
    line = inp[i]
    if line.startswith("seeds:"):
        seeds = [x for x in parse_positive_ints_str(line)]
        i+=1
        continue
    if "map" in line or line == "":
        changed = [False] * len(seeds)
        i+=1
        continue
    info = parse_positive_ints_str(line)
    dest_start = info[0]
    source_start = info[1]
    r = info[2]
    for index, kind in enumerate(seeds):
        if source_start <= kind < source_start + r and changed[index] == False:
            seeds[index] = dest_start + kind - source_start
            changed[index] = True
    i+=1

print(min(seeds))
