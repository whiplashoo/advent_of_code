def part_one(f):
    lines = f.readlines()
    letters_found = []
    tot_sum = 0
    i = 0
    while i < len(lines):
        if lines[i] != "\n":
            line = lines[i].strip()
            for letter in line:
                if letter not in letters_found:
                    letters_found.append(letter)
        else:
            tot_sum += len(letters_found)
            letters_found = []
        i += 1
    print(tot_sum)

def part_two(f):
    lines = f.readlines()
    letters_found = []
    group_answers = []
    tot_sum = 0
    i = 0
    while i < len(lines):
        if lines[i] != "\n":
            line = lines[i].strip()
            group_answers.append(line)
            for letter in line:
                if letter not in letters_found:
                    letters_found.append(letter)
        else:
            for letter in letters_found:
                if all(letter in group_answer for group_answer in group_answers):
                    tot_sum += 1
            group_answers = []
            letters_found = []
        i += 1
    print(tot_sum)

with open("day6.txt") as f:
    part_one(f)
    part_two(f)
