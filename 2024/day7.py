from aoc import input_as_lines
from itertools import product

inp = input_as_lines("day7.txt")

ops = ["+", "*"]
ops2 = ["+", "*", "|"]

def solve(arr, target):
    res = arr[0]
    operator = ""
    for x in arr[1:]:
        if not isinstance(x, int):
            operator = x
        else:
            if operator == "+":
                res += x
            elif operator == "*": 
                res *= x
            else:
                res = int(str(res) + str(x))
            if res > target:
                return None
    return res

def process_arr(nums, op, target):
    arr = []
    for idx, x in enumerate(nums):
        arr.append(x)
        if idx < len(nums) - 1:
            arr.append(op[idx])
    return solve(arr, target)
        
p1 = 0
p2 = 0
for line in inp:
    val = int(line.split(":")[0])
    nums = [int(x) for x in line.split(":")[1].split()]
    ops_list = product(ops, repeat = len(nums) - 1)
    for op in ops_list:
        result = process_arr(nums, op, val)
        if val == result:
            p1 += result
            break
    ops_list = product(ops2, repeat = len(nums) - 1)
    for op in ops_list:
        result = process_arr(nums, op, val)
        if val == result:
            p2 += result
            break

print(p1)
print(p2)


