from aoc import input_as_lines

inp = input_as_lines("day10.txt")

opens = ["[", "(", "{", "<"]
closes = ["]", ")", "}", ">"]

# PART 1
mapping = dict(zip(opens, closes))
q = []
score = 0
score_points = dict(zip(closes, [57, 3, 1197, 25137]))
invalids = []
for i in inp:
    line = [x for x in i]
    for char in line:
        if char in opens:
            q.append(mapping[char])
        elif char in closes:
            if q == [] or char != q.pop():
                score += score_points[char]
                invalids.append(inp.index(i))
                break
print(score)

# PART 2


def score_rem(q):
    scores = dict(zip(closes, [2, 1, 3, 4]))
    s = 0
    for i in q:
        s *= 5
        s += scores[i]
    return s


all_scores = []
for i in inp:
    if inp.index(i) not in invalids:
        line = [x for x in i]
        q = []
        for char in line:
            if char in opens:
                q.append(mapping[char])
            elif char in closes:
                last_occ = len(q) - 1 - q[::-1].index(char)
                del q[last_occ]
        all_scores.append(score_rem(q[::-1]))
print(sorted(all_scores)[len(all_scores) // 2])
