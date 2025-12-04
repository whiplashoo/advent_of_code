from aoc import input_as_lines
from itertools import combinations
import functools

inp = input_as_lines("day3.txt")
p1 = 0

for line in inp:
	bank = [int(x) for x in line]
	comb = combinations(bank, 2)
	mj = 0
	for c in comb:
		mj = max((c[0] * 10) + c[1], mj)
	p1 += mj

print(p1)

@functools.cache
def get_joltage(a):
	length = len(a)
	s = 0
	for ind, c in enumerate(a):
		s += c * (10 ** (length - ind - 1))
	return s


p2 = 0
for line in inp:
	bank = [int(x) for x in line]
	length = len(bank)
	mj = 0
	for i in range(12, 13):
		comb = combinations(bank, i)
		for c in comb:
			# strc = "".join([str(x) for x in c])
			# intc = int(strc)
			ss = get_joltage(c)
			print(ss)
			mj = max(mj, ss)
	p2 += mj

print(p2)
