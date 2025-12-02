from aoc import input_as_string


inp = input_as_string("day2.txt")
p1 = 0
p2 = 0

ids = inp.split(",")

def is_invalid(n):
	strn = str(n)
	length = len(strn)
	if length % 2 == 0:
		part1 = strn[:length//2]
		part2 = strn[length//2:]
		if part1 == part2:
			return True
	return False 

def check_parts(nn, step, part, length):
	for i in range(step, length, step):
		pp = nn[i: i+step]
		if pp != part:
			return False
	return True 


def is_invalid2(n):
	strn = str(n)
	length = len(strn)
	for step in range(1, length//2 + 1):
		part = strn[0:step]
		if check_parts(strn, step, part, length):
			return True
	return False


for rr in ids:
	start, end = [int(x) for x in rr.split("-") ]
	for n in range(start, end + 1):
		if is_invalid(n):
			p1 += n
		if is_invalid2(n):
			p2 += n


print(p1)
print(p2)

