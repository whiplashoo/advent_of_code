from collections import deque

from aoc import input_as_lines, parse_positive_ints_str

inp = input_as_lines("day5.txt")

stacks_count = (len(inp[0]) + 1) // 4

stacks = [deque() for _ in range(stacks_count)]

# PART 1
for line in inp:
    if line == "" or line[1] == "1":
        pass
    elif line[0] == "m":
        p = parse_positive_ints_str(line)
        fromc = p[1] - 1
        toc = p[2] - 1
        count = p[0]
        for c in range(count):
            el = stacks[fromc].pop()
            stacks[toc].append(el)
    else:
        stack_no = 0
        i = 0
        while i < len(line):
            el = line[i:i+3]
            if el != "   ":
                stacks[stack_no].appendleft(el)
            i += 4
            stack_no += 1

ret = ""
for stack in stacks:
    ret += stack[-1].replace("[", "").replace("]", "")
print(ret)

# PART 2
stacks = [deque() for _ in range(stacks_count)]
for line in inp:
    if line == "" or line[1] == "1":
        pass
    elif line[0] == "m":
        p = parse_positive_ints_str(line)
        fromc = p[1] - 1
        toc = p[2] - 1
        count = p[0]
        move_d = deque()
        for c in range(count):
            el = stacks[fromc].pop()
            move_d.append(el)
        for c in range(count):
            stacks[toc].append(move_d.pop())
    else:
        stack_no = 0
        i = 0
        while i < len(line):
            el = line[i:i+3]
            if el != "   ":
                stacks[stack_no].appendleft(el)
            i += 4
            stack_no += 1

ret = ""
for stack in stacks:
    ret += stack[-1].replace("[", "").replace("]", "")
print(ret)
