from aoc import input_as_string
from math import prod
inp = input_as_string("day16.txt")


def hex2bin(hex):
    return bin(int(hex, 16))[2:].zfill(4)


versions = 0


def parse(binary, i):
    global versions
    V = int(binary[i:i+3], 2)
    versions += V
    T = int(binary[i+3:i+6], 2)

    if T == 4:
        i += 6
        bin_literal = ""
        while True:
            bin_literal += binary[i+1:i+5]
            if binary[i] == "1":
                i += 5
            elif binary[i] == "0":
                i += 5
                val_literal = int(bin_literal, 2)
                break
        return val_literal, i
    else:
        # Operator packet
        i += 6
        I = binary[i]
        i += 1
        sub_packets = []
        if I == "0":
            length = int(binary[i:i+15], 2)
            start_i = i + 15
            i = start_i
            while True:
                val_literal, next_i = parse(binary, i)
                sub_packets.append(val_literal)
                i = next_i
                if next_i - start_i == length:
                    break
        else:
            count = int(binary[i:i+11], 2)
            i += 11
            for j in range(count):
                val_literal, next_i = parse(binary, i)
                sub_packets.append(val_literal)
                i = next_i
        if T == 0:
            return sum(sub_packets), i
        elif T == 1:
            return prod(sub_packets), i
        elif T == 2:
            return min(sub_packets), i
        elif T == 3:
            return max(sub_packets), i
        elif T == 5:
            return (1 if sub_packets[0] > sub_packets[1] else 0), i
        elif T == 6:
            return (0 if sub_packets[0] > sub_packets[1] else 1), i
        elif T == 7:
            return (1 if sub_packets[0] == sub_packets[1] else 0), i


binary = "".join([hex2bin(x) for x in inp])
v, i = parse(binary, 0)
print(versions)
print(f"RESULT: value {v}")
