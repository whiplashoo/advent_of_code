from aoc import input_as_ints

# PART 1
res = sum([x//3 - 2 for x in input_as_ints("day1.txt")])
print(res)


# PART 2
def calc_rec(x):
    return 0 if x <= 0 else x + calc_rec(x//3 - 2)


res = sum([calc_rec(x) - x for x in input_as_ints("day1.txt")])

print(res)
