from math import gcd


def compute_lcm(a):
    lcm = a[0]
    for i in a[1:]:
        lcm = lcm * i // gcd(lcm, i)
    return lcm


def part_one(timestamp, ids):
    buses = [int(i) for i in ids if i != 'x']
    wait_times = []
    for bus in buses:
        prev_bus = timestamp // bus * bus
        wait_times.append(prev_bus + bus - timestamp)
    return min(wait_times) * buses[wait_times.index(min(wait_times))]


def part_two(ids):
    buses = []
    for bus in ids:
        if bus != 'x':
            buses.append(int(bus))
        else:
            buses.append('x')
    timestamp = 0
    matched_buses = [buses[0]]
    while True:
        timestamp += compute_lcm(matched_buses)
        print(timestamp)
        for i, bus in enumerate(buses):
            if bus != 'x':
                if (timestamp + i) % bus == 0:
                    if bus not in matched_buses:
                        matched_buses.append(bus)
        if len(matched_buses) == len(buses) - buses.count('x'):
            break

    return timestamp


with open("day13.txt") as f:
    inp = f.readlines()
    print(part_one(int(inp[0]), inp[1].split(',')))
    print(part_two(inp[1].split(',')))
