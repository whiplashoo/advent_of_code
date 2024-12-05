from aoc import input_as_lines
from collections import defaultdict
from functools import cmp_to_key

inp = input_as_lines("day5.txt")

# PARSING
befores = defaultdict(list)
afters = defaultdict(list)
updates = []
end_rules = False
for line in inp:
    if line == "":
        end_rules = True
        continue
    if not end_rules:
        sp = line.split("|")
        afters[sp[0]].append(sp[1])
        befores[sp[1]].append(sp[0])
    else:
        updates.append(line.split(","))

print(befores)
print(afters)
# P1
def is_correct(update):
    correct = True
    for i in range(len(update)):
        to_check = update[i]
        for b in range(0, i):
            if update[b] in afters[to_check]:
                correct = False
                break
        for a in range(i+1, len(update)):
            if update[a] in befores[to_check]:
                correct = False
                break
    return correct

p1 = 0 
p2 = 0
dependencies = set()
for x, y in afters.items():
    for y_page in y:
        dependencies.add((x, y_page))

def compare_pages(x, y):
    if (x, y) in dependencies:
        return -1 
    elif (y, x) in dependencies:
        return 1
    else:
        return 0
    
for update in updates:
    if is_correct(update):
        p1 += int(update[len(update) // 2])
    else:
        corrected_order = sorted(update, key=cmp_to_key(compare_pages))
        p2 += int(corrected_order[len(corrected_order) // 2])

print(p1)
print(p2)

