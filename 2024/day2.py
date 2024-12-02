from aoc import input_as_lines, parse_positive_ints_str

inp = input_as_lines("day2.txt")
p1 = 0
p2 = 0

def is_safe(levels):
    if levels == sorted(levels) or levels == sorted(levels, reverse=True):
        for i in range(len(levels) - 1):
            diff = abs(levels[i] - levels[i+1]) 
            if diff < 1 or diff > 3:
                return False
        return True
    return False

def get_perm_list(x, i):
    perm = []
    for j in range(len(x)):
        if i == j: continue
        perm.append(x[j])
    return perm

#PART 1 & 2
for line in inp:
    levels = parse_positive_ints_str(line)
    if is_safe(levels):
        p1 += 1
    else:
        is_safe_by_removing = False
        for i in range(len(levels)):
            perm = get_perm_list(levels, i)
            if is_safe(perm):
                p2 += 1
                break
                
print(p1)
print(p1 + p2)