from aoc import input_as_lines

report = input_as_lines("day3.txt")

# PART 1
report_length = len(report[0])
switches = [0] * report_length
for i in range(report_length):
    for j in range(len(report)):
        if report[j][i] == "1":
            switches[i] += 1
        else:
            switches[i] -= 1

gamma_rate = int("".join(["1" if x > 0 else "0" for x in switches]), 2)
epsilon_rate = int("".join(["0" if x > 0 else "1" for x in switches]), 2)
print(gamma_rate * epsilon_rate)


# PART 2
for_oxygen = list(report)
for_co2 = list(report)
for i in range(report_length):
    if len(for_oxygen) > 1:
        a0 = len([r for r in for_oxygen if r[i] == '0'])
        a1 = len([r for r in for_oxygen if r[i] == '1'])
        if a1 >= a0:
            for_oxygen = [r for r in for_oxygen if r[i] == '1']
        else:
            for_oxygen = [r for r in for_oxygen if r[i] == '0']
    if len(for_co2) > 1:
        b0 = len([r for r in for_co2 if r[i] == '0'])
        b1 = len([r for r in for_co2 if r[i] == '1'])
        if b1 >= b0:
            for_co2 = [r for r in for_co2 if r[i] == '0']
        else:
            for_co2 = [r for r in for_co2 if r[i] == '1']


oxygen = int(for_oxygen[0], 2)
co2 = int(for_co2[0], 2)
print(oxygen*co2)
