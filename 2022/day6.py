from aoc import input_as_string

inp = input_as_string("day6.txt")


def calc(chars_count):
    n = chars_count
    while True:
        if len(set(inp[n - chars_count:n])) == chars_count:
            print(n)
            break
        n += 1
        if n == len(inp):
            break


# PART 1
calc(4)

# PART 2
calc(14)
