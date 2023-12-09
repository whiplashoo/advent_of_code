from aoc import input_as_lines, parse_ints_str

inp = input_as_lines("day9.txt")

s1 = 0
last_ints = []
for line in inp:
    seq = parse_ints_str(line)
    last_ints.append(seq[-1])
    while True:
        new_seq = []
        for i in range(len(seq) - 1):
            new_seq.append(seq[i+1] - seq[i])
        last_ints.append(new_seq[-1])
        if all(n == 0 for n in new_seq):
            s1 += sum(last_ints)
            last_ints = []
            break
        seq = new_seq

print(s1)

#PART 2
s2 = 0
first_ints = []
for line in inp:
    seq = parse_ints_str(line)
    first_ints.append(seq[0])
    while True:
        new_seq = []
        for i in range(len(seq) - 1):
            new_seq.append(seq[i+1] - seq[i])
        first_ints.append(new_seq[0])
        if all(n == 0 for n in new_seq):
            ss = 0
            first_ints = list(reversed(first_ints))
            for i in range(len(first_ints) - 1):
                first_ints[i+1] -= first_ints[i]
            s2 += first_ints[-1]
            first_ints = []
            break
        seq = new_seq
print(s2)
