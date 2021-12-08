from aoc import input_as_lines, print_matrix
from itertools import permutations
from copy import deepcopy

inp = input_as_lines("day8.txt")

# PART 1
count = 0
for a in inp:
    digits = [len(x) for x in a.split("|")[1].strip().split()]
    for d in digits:
        if d in [2, 3, 4, 7]:
            count += 1
print(count)

# PART 2


def letters_in_string(arr, string):
    return all([x in string for x in arr])


def fill_digit(digit, string, signals):
    for i in range(len(string)):
        positions[digit][i] = s[i]
    signals.remove(string)


def is_position_filled(digit):
    return not all([x == 0 for x in positions[digit]])


def solution_found():
    return all([is_position_filled(x) for x in range(10)])


def is_digit_2(string, signals):
    others = set("abcdefg").difference(string)
    for letter in others:
        found = 0
        for s in signals:
            if letter in s:
                found += 1
        if found == 9:
            return True
    return False


def is_digit_9(string):
    other = set("abcdefg").difference(string).pop()
    if other in positions[2] and other not in positions[3] and other not in positions[1] and other not in positions[4] and other not in positions[5]:
        return True
    return False


def is_digit_6(string):
    other = set("abcdefg").difference(string).pop()
    if other not in positions[5] and other in positions[1]:
        return True
    return False


final_sum = 0
for a in inp:
    positions = [
        [0]*6,
        [0]*2,
        [0]*5,
        [0]*5,
        [0]*4,
        [0]*5,
        [0]*6,
        [0]*3,
        [0]*7,
        [0]*6,
    ]
    signals = a.split("|")[0].strip().split()
    original_signals = deepcopy(signals)
    signals.sort(key=lambda x: len(x))
    i = 0
    while signals != []:
        s = signals[i]
        if len(s) == 2:
            fill_digit(1, s, signals)
        elif len(s) == 3:
            fill_digit(7, s, signals)
        elif len(s) == 4:
            fill_digit(4, s, signals)
        elif len(s) == 5:
            if letters_in_string(positions[1], s):
                fill_digit(3, s, signals)
                i = 0
            elif is_digit_2(s, original_signals):
                fill_digit(2, s, signals)
                i = 0
            elif is_position_filled(2) and is_position_filled(3):
                fill_digit(5, s, signals)
                i = 0
            else:
                i += 1
        elif len(s) == 6:
            if is_position_filled(6) and is_position_filled(9):
                fill_digit(0, s, signals)
                i = 0
            elif is_digit_9(s):
                fill_digit(9, s, signals)
                i = 0
            elif is_digit_6(s):
                fill_digit(6, s, signals)
                i = 0
            else:
                i += 1
        elif len(s) == 7:
            fill_digit(8, s, signals)
    digits = a.split("|")[1].strip().split()
    outp = ""
    for d in digits:
        for p in positions:
            if set(d) == set(p):
                outp += str(positions.index(p))
    final_sum += int(outp)

print(final_sum)
