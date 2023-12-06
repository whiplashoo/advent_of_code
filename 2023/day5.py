from collections import defaultdict

from aoc import input_as_lines, parse_positive_ints_str

inp = input_as_lines("day5t.txt")

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

seeds = []
seeds2 = []

pairs = []
i = 0
while i < len(inp):
    line = inp[i]
    print(line)
    if line.startswith("seeds:"):
        seeds = [x for x in parse_positive_ints_str(line)]
        for j in range(0, len(seeds), 2):
            pairs.append([seeds[j], seeds[j] + seeds[j + 1]])
            num = seeds[j]
            for k in range(seeds[j + 1]):
                seeds2.append(num + k)
        i+=1
        print(pairs)
        print(seeds2)
        continue
    if "map" in line or line == "":
        changed = [False] * len(seeds2)
        changedSS = [{False, False}] * len(pairs)
        i+=1
        continue
    info = parse_positive_ints_str(line)
    dest_start = info[0]
    source_start = info[1]
    r = info[2]
    source_end = source_start + r
    print(f"source_start-end: {source_start} - {source_end}")
    print(f"Before: {pairs}")
    print(seeds2)
    new_pairs = []
    for index, (pair_start, pair_end) in enumerate(pairs):
        if pair_start >= source_start and pair_start < source_end:
            pairs[index][0] += dest_start - source_start
            if pair_end <= source_end:
                pairs[index][1] += dest_start - source_start
        elif pair_end >= source_start and pair_end < source_end:

    #     elif pair_end < source_end and pair_end >= source_end:
    #         pairs[index][1] = dest_start + pair_start - source_start

    for index, kind in enumerate(seeds2):
        if source_start <= kind < source_start + r and changed[index] == False:
            seeds2[index] = dest_start + kind - source_start
            changed[index] = True
    print(f"After: {pairs}")
    print(seeds2)
    print()
    i+=1
    
print(ss)
print(min(seeds2))