from aoc import input_as_lines


inp = input_as_lines("day2.txt")

p1 = 0
p2 = 0

for line in inp:
	l,w,h = [int(x) for x in line.split("x")]
	p1 += 2*l*w + 2*w*h + 2*h*l
	p1 += min(min(l * w,w * h) , h * l)
	ss = sorted([l,w,h])
	p2 += ss[0] + ss[0] + ss[1] + ss[1]
	p2 += l*w*h

print(p1)
print(p2)
