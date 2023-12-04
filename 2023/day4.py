from collections import defaultdict

from aoc import input_as_lines, parse_positive_ints_str

inp = input_as_lines("day4.txt")

total = 0
card_num = 1
scores = {}

for line in inp:
    line = line.split(": ")[1]
    line = line.split(" | ")
    w = set(parse_positive_ints_str(line[0]))
    p = set(parse_positive_ints_str(line[1]))
    u = set.intersection(w,p)
    scores[card_num] = len(u) # for Part 2
    card_num += 1 # for Part 2
    if (len(u) > 0):
        total += 2 ** (len(u) - 1)

print(int(total))

# PART 2
count = card_num
count_cards = defaultdict(lambda:1)

for id, wins in scores.items():
    for i in range(count_cards[id]):
        for j in range(wins):
            if (id + j + 1) < count:
                count_cards[id + j + 1] += 1
print(sum(count_cards.values()))