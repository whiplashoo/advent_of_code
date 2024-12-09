from aoc import input_as_lines
from itertools import product

inp = input_as_lines("day7t.txt")

ops = ["+", "*"]

def solve(arr):
    res = arr[0]
    sum = True
    for x in arr[1:]:
        if x == "*":
            sum = False
        elif x == "+":
            sum = True
        else:
            if sum:
                res += x
            else: 
                res *= x
    return res

def process_arr(nums, op):
    arr = []
    for idx, x in enumerate(nums):
        arr.append(x)
        if idx < len(nums) - 1:
            arr.append(op[idx])
    print(arr)
    return solve(arr)
        
p1 = 0
for line in inp:
    val = int(line.split(":")[0])
    nums = [int(x) for x in line.split(":")[1].split()]
    ops_list = product(ops, repeat = len(nums) - 1)
    for op in ops_list:
        result = process_arr(nums, op)
        if val == result:
            p1 += result

print(p1)


