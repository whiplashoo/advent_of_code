from aoc import input_as_lines

inp = input_as_lines("day2.txt")

# PART 1
score = 0
my_play = {"X": 1, "Y": 2, "Z": 3}
wins = ["AY", "BZ", "CX"]
draws = ["AX", "BY", "CZ"]
losses = ["AZ", "BX", "CY"]

for line in inp:
    me = line[2]
    play = line.replace(" ", "")
    if play in wins:
        score += 6
    elif play in draws:
        score += 3
    score += my_play[me]
print(score)

# PART 2
score = 0
strategy = {
    "X": losses,
    "Y": draws,
    "Z": wins
}
res = {"X": 0, "Y": 3, "Z": 6}
for line in inp:
    opp = line[0]
    expected = line[2]
    for play in strategy[expected]:
        if play[0] == opp:
            score += my_play[play[1]]
    score += res[expected]
print(score)
