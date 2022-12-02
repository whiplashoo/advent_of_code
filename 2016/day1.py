from aoc import input_as_string

inp = input_as_string("day1.txt")

inst = [i.strip() for i in inp.split(",")]

facing = "N"
x = 0
y = 0

for instruction in inst:
    dir = instruction[0]
    bl = int(instruction[1])
    if facing == "N":
        if dir == "R":
            x += bl
            facing = "E"
        else:
            x -= bl
            facing = "W"
    elif facing == "E":
        if dir == "R":
            y -= bl
            facing = "S"
        else:
            y += bl
            facing = "N"
    elif facing == "S":
        if dir == "R":
            x -= bl
            facing = "W"
        else:
            x += bl
            facing = "E"
    elif facing == "W":
        if dir == "R":
            y += bl
            facing = "N"
        else:
            y -= bl
            facing = "S"

print(x, y)
print(abs(x) + abs(y))
