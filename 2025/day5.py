from aoc import input_as_lines

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

for f, l in rs:
	