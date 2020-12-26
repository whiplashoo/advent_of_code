def part_one(timestamp, ids):
    buses = [int(i) for i in ids if i != 'x']
    wait_times = []
    for bus in buses:
        prev_bus = timestamp // bus * bus
        wait_times.append(prev_bus + bus - timestamp)
    return min(wait_times) * buses[wait_times.index(min(wait_times))]


def part_two(instructions):
    pass


with open("day13.txt") as f:
    inp = f.readlines()
    print(inp[0])
    print(inp[1])
    print(part_one(int(inp[0]), inp[1].split(',')))
    print(part_two(inp))
