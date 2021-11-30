from copy import deepcopy

def part_one(instructions):
    i = 0
    acc = 0
    executed = []
    while True:
        if i == len(instructions) or i in executed:
            break
        else:
            executed.append(i)
        if 'acc' in instructions[i]:
            acc += int(instructions[i].split(" ")[1])
        elif 'jmp' in instructions[i]:
            i += int(instructions[i].split(" ")[1])
            continue
        i += 1    
    return i, acc

def part_two(instructions):
    for n, item in enumerate(instructions):
        if 'nop' in item or 'jmp' in item:
            new_instructions = deepcopy(instructions)
            if 'nop' in item:
                new_instructions[n] = 'jmp ' + new_instructions[n].split(" ")[1]
            if 'jmp' in item:
                new_instructions[n] = 'nop ' + new_instructions[n].split(" ")[1]
            p2 = part_one(new_instructions)
            if p2[0] == len(instructions):
                break
        else:
            continue
    return p2

with open("day8.txt") as f:
    instructions = []
    for line in f:
        instructions.append(line.strip())
    print(part_one(instructions))
    print(part_two(instructions))
