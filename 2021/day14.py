from aoc import input_as_lines, print_matrix
from collections import Counter, defaultdict

inp = input_as_lines("day14.txt")

# PARSE
pairs = {}
for line in inp:
    if line == "":
        continue
    elif "->" in line:
        s = [x.strip() for x in line.split("->")]
        pairs[s[0]] = s[1]
    else:
        t = line.strip()

# GET STARTER STRING AND CONSTRUCT MEMO DICTIONARY
tt = []
memo = {}
for i in range(len(t) - 1):
    tt.append(t[i] + t[i+1])
    s = t[i] + t[i+1]
    s1 = t[i] + pairs[s]
    s2 = pairs[s] + t[i+1]
    memo[s] = [s1, s2]

while True:
    filled_memo = True
    for ss in list(memo.values()):
        for s in ss:
            if s not in list(memo.keys()):
                filled_memo = False
                s1 = s[0] + pairs[s]
                s2 = pairs[s] + s[1]
                memo[s] = [s1, s2]
    if filled_memo:
        break

# PART 1 & 2: PERFORM INSERTIONS
tt_count = Counter(tt)
for i in range(40):
    new_count = defaultdict(int)
    for t in list(tt_count.keys()):
        new_count[memo[t][0]] += tt_count[t]
        new_count[memo[t][1]] += tt_count[t]
    tt_count = new_count

# COUNT SCORES
scores = defaultdict(int)
for t in tt_count.keys():
    scores[t[0]] += tt_count[t]
last_char = t[-1]
scores[last_char] += 1

mc = max(scores.values())
lc = min(scores.values())
print(mc - lc)
