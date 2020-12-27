def apply_mask(val, mask):
    retval = ''
    for v, m in zip(val, mask):
        if m == '0':
            retval += '0'
        elif m == '1':
            retval += '1'
        else:
            retval += v
    return int(retval, 2)


def part_one(inp):
    mem = {}
    for line in inp:
        line = line.strip()
        if 'mask' in line:
            mask = line.split('=')[1][1:]
        else:
            pos = line.split('[')[1].split(']')[0]
            val = line.split('=')[1][1:]
            val = bin(int(val))[2:].zfill(36)
            mem[pos] = apply_mask(val, mask)
    return (sum(mem.values()))


def part_two(ids):
    pass


with open("day14.txt") as f:
    inp = f.readlines()
    print(part_one(inp))
    # print(part_two(inp[1].split(',')))
