import math
from collections import defaultdict

from aoc import input_as_lines, parse_positive_ints_str

inp = input_as_lines("day11.txt")

monkeys = []


class Monkey:
    def __init__(self, name):
        self.name = name
        self.items = []
        self.op = tuple()
        self.divisible = 1
        self.t = name
        self.f = name

    def __repr__(self):
        return f"Monkey {self.name} \n with items {self.items} \n op: {self.op} \n test: div by {self.divisible} \n if true to: {self.t} \n if false to: {self.f}"


def apply_operation(operation, operand, input):
    if operation == "+":
        return input + operand
    else:
        return input * operand


# PART 1
for line in inp:
    if line == "":
        continue
    if line.startswith("Monkey"):
        m_id = len(monkeys)
        monkeys.append(Monkey(name=m_id))
    elif "Starting" in line:
        monkeys[-1].items = parse_positive_ints_str(line)
    elif "Operation" in line:
        operator = "+" if "+" in line else "*"
        nums = parse_positive_ints_str(line)
        operand = nums[0] if len(nums) > 0 else "self"
        monkeys[-1].op = (operator, operand)
    elif "Test" in line:
        monkeys[-1].divisible = parse_positive_ints_str(line)[0]
    elif "true" in line:
        monkeys[-1].t = parse_positive_ints_str(line)[0]
    elif "false" in line:
        monkeys[-1].f = parse_positive_ints_str(line)[0]
rounds = 0
inspected = [0 for _ in range(len(monkeys))]
while rounds < 20:
    for m in monkeys:
        for worry in m.items:
            inspected[monkeys.index(m)] += 1
            worry = apply_operation(
                m.op[0], worry if m.op[1] == "self" else m.op[1], worry)
            worry = math.floor(worry/3)
            if worry % m.divisible == 0:
                monkeys[m.t].items.append(worry)
            else:
                monkeys[m.f].items.append(worry)
        m.items = []
    rounds += 1

ret = sorted(inspected, reverse=True)
print(ret[0] * ret[1])
