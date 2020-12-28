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
    last_indexes = {}
    for index, num in enumerate(inp):
        last_indexes[num] = index + 1
    cur_index = len(inp)
    last_said = inp[-1]
    while cur_index < 30000000:
        if last_said not in last_indexes.keys():
            last_indexes[last_said] = cur_index
            last_said = 0
        else:
            diff = cur_index - last_indexes[last_said]
            last_indexes[last_said] = cur_index
            last_said = diff
        cur_index += 1
    return last_said


inp = [18, 8, 0, 5, 4, 1, 20]
print(part_one(inp))
print(part_two(inp))
