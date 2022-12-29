from aoc import input_as_lines, parse_ints_str

inp = input_as_lines("day21t.txt")

m = {}

for line in inp:
    split = line.split(":")
    monkey = split[0]
    s = split[1].strip()
    if len(s) <= 4:
        m[monkey] = int(s)
    elif "+" in s:
        m[monkey] = s.split(" + ") + ["+"]
    elif "-" in s:
        m[monkey] = s.split(" - ") + ["-"]
    elif "*" in s:
        m[monkey] = s.split(" * ") + ["*"]
    elif "/" in s:
        m[monkey] = s.split(" / ") + ["/"]


def recurse(monkey):
    cur_mon = m[monkey]
    if isinstance(cur_mon, int):
        return cur_mon
    mon1 = recurse(cur_mon[0])
    mon2 = recurse(cur_mon[1])
    if cur_mon[2] == "+":
        return mon1 + mon2
    if cur_mon[2] == "-":
        return mon1 - mon2
    if cur_mon[2] == "*":
        return mon1 * mon2
    if cur_mon[2] == "/":
        return mon1 // mon2


a = recurse("root")
print(a)

# PART 2
n = []
sol = {}


def find_eq(monkey):
    global n
    cur_mon = m[monkey]
    if isinstance(cur_mon, int):
        return cur_mon
    n.append(cur_mon[1])
    n.append(cur_mon[2])
    n.append(cur_mon[0])

    mon1 = find_eq(cur_mon[0])
    mon2 = find_eq(cur_mon[1])
    if cur_mon[2] == "+":
        return mon1 + mon2
    if cur_mon[2] == "-":
        return mon1 - mon2
    if cur_mon[2] == "*":
        return mon1 * mon2
    if cur_mon[2] == "/":
        return mon1 // mon2

# Basically what I do is I traverse the tree and collect all the operations from the left side of the equation that I will have to apply to the result of the right side.
# So, for the example input, my code would collect a list of["- 3", "2 *", "4 +", "/ 4"]. Then I apply these operation in reversed order to the right side and get the final result.


m["root"][2] = "="
#m["humn"] = "hymn"

aa = find_eq("pppw")
print(n)
# monkey = "pppw"
# while monkey != "hymn":
#     cur_mon = m[monkey]
#     print(cu)
#     if isinstance(cur_mon, int):
#         n.append(cur_mon)
#     else:
#         n.append(cur_mon[0])
#         n.append(cur_mon[2])
#         n.append(cur_mon[1])
print(n)
