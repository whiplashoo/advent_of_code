from aoc import input_as_string, parse_ints_str
import copy

inp = parse_ints_str(input_as_string("day2.txt"))


def calc(noun, verb):
    mem = copy.deepcopy(inp)
    mem[1] = noun
    mem[2] = verb
    i = 0
    try:
        while mem[i] != 99:
            if mem[i] == 1:
                mem[mem[i+3]] = mem[mem[i+1]] + mem[mem[i+2]]
            elif mem[i] == 2:
                mem[mem[i+3]] = mem[mem[i+1]] * mem[mem[i+2]]
            i += 4
    except IndexError:
        return
    return mem[0]


# PART 1
print(calc(12, 2))

# PART 2
for i in range(100):
    for j in range(100):
        res = calc(i, j)
        if res == 19690720:
            print(100 * i + j)
            break
