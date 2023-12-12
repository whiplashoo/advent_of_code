from itertools import product

from aoc import input_as_lines, parse_positive_ints_str

inp = input_as_lines("day12.txt")


def is_valid(s, arrange):
    occ = []
    current = 0
    for i in s:
        if i == ".":
            if current != 0:
                occ.append(current)
            current = 0
            continue
        else:
            current += 1
    if current != 0:
        occ.append(current)
    return occ == arrange
    
def get_products(length):
    return set(product(".#", repeat= length))

def get_replaced_arr(arr, perm):
    replaced_arr = arr[:]
    for p in perm:
        replaced_arr[replaced_arr.index("?")] =  p
    return replaced_arr

s = 0
for line in inp:
    arrange = parse_positive_ints_str(line)
    spring = [x for x in line.split(" ")[0]]
    #print(spring, arrange)
    qs = spring.count("?")
    for perm in get_products(qs):
        new_spring = get_replaced_arr(spring, perm)
        if is_valid(new_spring, arrange):
            s += 1
        
print(s)