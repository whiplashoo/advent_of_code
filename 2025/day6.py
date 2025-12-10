from aoc import input_as_lines, parse_ints_str, print_matrix
from functools import reduce

inp = input_as_lines("day6.txt")

got_symbols = False
s = []

p1 = []

for line in inp[::-1]:
	if not got_symbols:
		s = line.split()
		for i in range(len(s)):
			p1.append(0 if s[i] == "+" else 1)
		got_symbols = True
	else:
		nums = parse_ints_str(line)
		for idx, num in enumerate(nums):
			if s[idx] == "*":
				p1[idx] *= nums[idx]
			else:
				p1[idx] += nums[idx]

print(sum(p1))


# PART 2
p2 = 0
nums = []
N = []

for line in inp:
	N.append([c for c in line])

ROWS = len(N)
COLS = len(N[0])
nums = []

for c in range(COLS - 1, -1, -1):
	tmp = ""
	for r in range(ROWS):
		a = N[r][c]
		if r == ROWS - 1 and len(tmp) != 0:
			nums.append(tmp)
		if a == " " or a == "": continue
		if a == "*":
			mm = reduce(lambda x,y: int(x) * int(y), nums)
			p2 += mm
			nums =[]
			continue
		if a == "+":
			ss = sum(int(i) for i in nums)
			p2 += ss
			nums = []
			continue
		tmp += a

print(p2)