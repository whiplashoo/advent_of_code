from aoc import input_as_string
from collections import defaultdict
from copy import deepcopy
import time

inp = input_as_string(filename="day9t.txt")
blocks = defaultdict(lambda: ".")
is_file = True
i = 0
n = 0
id = 0

while i < len(inp):
    count = int(inp[i])
    for j in range(count):
        if is_file:
            blocks[n] = id
        n += 1
    if is_file:
        id += 1
    is_file = not is_file
    i += 1

def print_block(d):
    print("".join([str(d[x]) for x in range(n)]))

blocks2 = deepcopy(blocks)

right = n - 1
left = 0

while left < right:
    print(left, right, blocks[left], blocks[right])
    if blocks[left] == ".":
        while blocks[right] == ".":
            right -= 1
        blocks[left] = blocks[right]
        blocks[right] = "."
    left += 1

p1 = 0
for i in range(n):
    if blocks[i] != ".":
        p1 += i * blocks[i]
print(p1)

print_block(blocks2)

right = n - 1
left = 0

# while left < right:
#     print(left, right, blocks2[left], blocks2[right])
#     print_block(blocks2)
#     #time.sleep(0.5)
#     if blocks2[left] == ".":
#         left_len = 0
#         temp_left = left
#         while blocks2[temp_left] == ".":
#             left_len += 1
#             temp_left += 1
#         while blocks2[right] == ".":
#             right -= 1
#         right_len = 0
#         temp_right = right
#         while blocks2[temp_right] == blocks2[right]:
#             temp_right -= 1
#             right_len += 1
#         print(f"left_len {left_len}  + right_len {right_len}")
#         if right_len <= left_len:
#             for i in range(right_len):
#                 blocks2[left + i] = blocks2[right - i]
#                 blocks2[right - i] = "."
#                 print(f"swapping {left +i} with {right + i}")
#             left += right_len
#             right -= right_len
#         else:
#             left += right_len
#             right -= right_len
#     else:
#         left += 1

while right > 4:
    print(left, right, blocks2[left], blocks2[right])
    print_block(blocks2)
    left = 0
    time.sleep(0.5)
    while blocks2[right] == ".":
        right -= 1
    right_len = 0
    temp_right = right
    while blocks2[temp_right] == blocks2[right]:
        temp_right -= 1
        right_len += 1
    while left < n - 1:
        while blocks2[left] != ".":
            left += 1
        left_len = 0
        temp_left = left
        while blocks2[temp_left] == ".":
            left_len += 1
            temp_left += 1
        if right_len <= left_len:
            for i in range(right_len):
                blocks2[left + i] = blocks2[right - i]
                blocks2[right - i] = "."
                print(f"swapping {left +i} with {right + i}")
            break
        left += left_len
        print(left)
    right -= right_len

print_block(blocks2)

