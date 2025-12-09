from aoc import input_as_lines, parse_ints_str

inp = input_as_lines("day6t.txt")

got_symbols = False
s = []

p1 = []

for line in inp[::-1]:
	print(line)
	if not got_symbols:
		s = line.split()
		for i in range(len(s)):
			p1.append(0 if s[i] == "+" else 1)
		got_symbols = True
	else:
		nums = parse_ints_str(line)
		print(nums)
		for idx, num in enumerate(nums):
			if s[idx] == "*":
				p1[idx] *= nums[idx]
			else:
				p1[idx] += nums[idx]

print(sum(p1))

p2 = []
got_symbols = False
s = []
			
for line in inp[::-1]:
	print(line)
	if not got_symbols:
		s = line.split()
		for i in range(len(s)):
			p1.append(0 if s[i] == "+" else 1)
		got_symbols = True
	else:
		nums = parse_ints_str(line)
		print(nums)
		for idx, num in enumerate(nums):
			if s[idx] == "*":
				p1[idx] *= nums[idx]
			else:
				p1[idx] += nums[idx]