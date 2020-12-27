def part_one(inp):
    while True:
        if inp.count(inp[-1]) == 1:
            inp.append(0)
        else:
            occurences = [index for index,
                          el in enumerate(inp) if el == inp[-1]]
            inp.append(occurences[-1] - occurences[-2])
        if len(inp) == 2020:
            break
    return inp[-1]


def part_two(inp):
    pass


with open("day14.txt") as f:
    inp = [18, 8, 0, 5, 4, 1, 20]
    print(part_one(inp))
    # print(part_two(inp))
