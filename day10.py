from collections import defaultdict


def part_one(nums):
    one_jolts = 0
    three_jolts = 0
    joltages = sorted(nums)
    for i in range(len(joltages) - 1):
        if joltages[i + 1] - joltages[i] == 1:
            one_jolts += 1
        elif joltages[i + 1] - joltages[i] == 3:
            three_jolts += 1
    one_jolts += 1
    three_jolts += 1
    print(one_jolts, three_jolts)
    return one_jolts * three_jolts


def part_two(nums):
    joltages = [0] + sorted(nums)
    joltages.append(joltages[-1] + 3)
    counts = defaultdict(int, {0: 1})
    for a, b in zip(joltages[1:], joltages):
        counts[a] = counts[a - 3] + counts[a - 2] + counts[a - 1]
    return counts[joltages[-1]]


with open("day10.txt") as f:
    nums = []
    for line in f:
        nums.append(int(line.strip()))
    print(part_one(nums))
    print(part_two(nums))
