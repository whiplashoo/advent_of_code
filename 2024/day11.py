from aoc import input_as_string, parse_positive_ints_str
from collections import defaultdict

inp = input_as_string("day11.txt")

a = parse_positive_ints_str(inp)
stones = defaultdict(int)
for n in a:
    stones[n] += 1

def blink_stones():
    stones_copy = dict(stones)
    for stone, count in stones_copy.items():
        if count == 0: continue
        if stone == 0:
            stones[1] += count
            stones[0] -= count
        elif len(str(stone)) % 2 == 0:
            txt = str(stone)
            stone1 = int(txt[:len(txt) // 2])
            stone2 = int(txt[len(txt) // 2:])
            stones[stone1] += count
            stones[stone2] += count
            stones[stone] -= count
        else:
            stones[stone] -= count
            stones[stone * 2024] += count

for i in range(75):
    blink_stones()

print(sum(stones.values()))

