from itertools import combinations

from aoc import input_as_lines, parse_ints_str

inp = input_as_lines("day19t.txt")

N = {}

for idx, line in enumerate(inp):
    n = parse_ints_str(line)[0]
    N[idx] = {"original": n, "cur_pos": idx, "cur_val": n}

length = idx + 1
print(N)


def print_N(N):
    final_N = {}
    for key, item in N.items():
        final_N[item["cur_pos"]] = item["cur_val"]
    for k in sorted(final_N.keys()):
        print(k, final_N[k])
    print("------------------")


for key, item in N.items():
    n = item["cur_val"]
    original = item["original"]
    cur_pos = item["cur_pos"]
    print("moving: " + str(original))
    if original > 0:
        for i in range(cur_pos + 1, cur_pos + original):
            print("cur", cur_pos, cur_pos + original)
            i = i % length
            next_i = (i + 1) % length
            N[i]["cur_pos"] = N[i]["cur_pos"] - 1
            N[i]["cur_val"] = N[next_i]["cur_val"]
    else:
        for i in range(cur_pos, cur_pos + original, -1):
            i = i % length
            prev_i = (i - 1) % length
            N[i]["cur_pos"] = N[i]["cur_pos"] + 1
            N[i]["cur_val"] = N[prev_i]["cur_val"]
    N[(cur_pos + original) % length]["cur_val"] = n
    print_N(N)


# for idx, n in enumerate(original):
#     print(f"Will move {n} in position {(idx + n) % len(original)}")
#     N.insert((idx + n + 1) % len(original), n)
#     del N[idx]
#     print(N)
