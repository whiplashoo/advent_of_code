from aoc import input_as_ints

depths = input_as_ints("day1.txt")

# PART 1
ret1 = 0
for i in range(1, len(depths)):
    if depths[i] > depths[i-1]:
        ret1 += 1
print(ret1)

# PART 2
ret2 = 0
for i in range(3, len(depths)):
    try:
        if depths[i] > depths[i-3]:
            ret2 += 1
    except IndexError:
        pass

print(ret2)
