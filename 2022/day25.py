from aoc import input_as_lines, parse_ints_str

inp = input_as_lines("day25t.txt")

vals = {
    "2": 2,
    "1": 1,
    "0": 0,
    "-": -1,
    "=": -2,
}

s = 0
for line in inp:
    snafu = line[::-1]
    for power, digit in enumerate(snafu):
        s += vals[digit] * pow(5, power)

print(s)
