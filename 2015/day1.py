from aoc import input_as_string


inp = input_as_string("day1.txt")


p1 = 0

for idx, c in enumerate(inp):
	p1 += 1 if c == "(" else -1
	if p1 == -1:
		print(idx + 1)

print(p1)