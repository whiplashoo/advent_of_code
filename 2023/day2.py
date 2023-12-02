import math

from aoc import input_as_lines

inp = input_as_lines("day2.txt")
sum = 0

cubes = {
    "red": 0,
    "green": 0,
    "blue": 0,
}

id = 1
#PART 1
for line in inp:
    line = line.split(": ")[1]
    sets = line.split("; ")
    is_valid = True
    for s in sets:
        cc = s.split(", ")
        for c in cc:
            c = c.split(" ")
            cubes[c[1]] += int(c[0])
        if cubes["red"] >12 or cubes["green"] >13 or cubes["blue"] > 14:
            is_valid = False
        cubes = {
            "red": 0,
            "green": 0,
            "blue": 0,
        }
    if is_valid:
        sum+=id
    id += 1
    

print(sum)

#PART 2
sum = 0
max_cubes = {
        "red": 0,
        "green": 0,
        "blue": 0,
    }
for line in inp:
    line = line.split(": ")[1]
    sets = line.split("; ")
   
    for s in sets:
        cc = s.split(", ")
        for c in cc:
            c = c.split(" ")
            cubes[c[1]] += int(c[0])
        for t in max_cubes.keys():
            max_cubes[t] = max(max_cubes[t], cubes[t])
        cubes = {
            "red": 0,
            "green": 0,
            "blue": 0,
        }
    sum += math.prod(max_cubes.values())
    max_cubes = {
        "red": 0,
        "green": 0,
        "blue": 0,
    }

print(sum)