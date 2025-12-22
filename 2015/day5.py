from aoc import input_as_lines


inp = input_as_lines("day5.txt")

vowels = [a for a in "aeiou"]
forb = ["ab", "cd", "pq" ,"xy"]

def count_vowels(s):
	v = 0
	for c in s:
		if c in vowels:
			v += 1
	return v 

def has_twin(s):
	for i in range(len(s) - 1):
		if s[i] == s[i+1]:
			return True
	return False

def has_forbidden(s):
	for f in forb:
		if f in s:
			return True
	return False

def is_good(s):
	return count_vowels(s) >= 3 and has_twin(s) and not has_forbidden(s)


p1 = 0

for s in inp:
	if is_good(s):
		p1 += 1

def pair2(s):
	for i in range(len(s) - 2):
		subs = s[i] + s[i + 1]
		if subs in s[i + 2:]:
			return True
	return False

def repeat_with_between(s):
	for i in range(len(s) - 2):
		if s[i] == s[i+2]:
			return True
	return False


def is_good2(s):
	return pair2(s) and repeat_with_between(s)

p2 = 0

for s in inp:
	if is_good2(s):
		p2 += 1


print(p1)
print(p2)