def is_valid(min_times, max_times, letter, password):
	if password.count(letter) <= max_times and password.count(letter) >= min_times:
		return True

def is_valid2(pos1, pos2, letter, password):
	if password[pos1-1] == letter and password[pos2-1] == letter:
		return False
	if password[pos1-1] == letter or password[pos2-1] == letter:
		return True	

with open("day2.txt") as f:
	valid = 0
	for line in f:
		line = line.split(" ")
		min_times = int(line[0].split("-")[0])
		max_times = int(line[0].split("-")[1])
		letter = line[1][0]
		password = line[2].strip()
		if is_valid2(min_times, max_times, letter, password):
			valid += 1 
	print(valid)


	
