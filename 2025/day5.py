from aoc import input_as_lines
from copy import deepcopy

inp = input_as_lines("day5t.txt")
p1 = 0

rs = []

for line in inp:
	if "-" in line:
		f, l = [int(x) for x in line.split("-")]
		rs.append((f,l))
	else:
		if line == "":
			continue
		else:
			a = int(line)
			for f,l in rs:
				if a >= f and a<=l:
					p1+=1
					break

			
print(rs)
print(p1)

p2 = 0

opt = []

while True:
	changed = False
	for f, l in rs:
		low, high = f, l
		for f2, l2 in rs:
			if (f,l) == (f2,l2):
				continue
			print((f,l), (f2,l2))
			if f2 < f and (l2 <= l and l2 >= f):
				low = f2
				high = l
				changed = True
			elif l2 > l and (f2 >= f and f2 <= l):
				low = f
				high = l2
				changed = True
		opt.append((low, high))
	if not changed:
		break
	rs = deepcopy(opt)  


print(opt)

print("Dd")