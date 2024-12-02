from aoc import input_as_lines, parse_positive_ints_str

inp = input_as_lines("day19.txt")

wf = {}
parts = []
    
parsing_parts = False
for line in inp:
    if line == "":
        parsing_parts = True
        continue
    if not parsing_parts:
        line = line.replace("}", "").split("{")
        rules = []
        rules_list = line[1].split(",")
        for r in rules_list:
            r = r.split(":")
            if len(r) == 1:
                rules.append(r[0])
            else:
                r0 = r[0].split("<") if "<" in r[0] else r[0].split(">")
                r1 = r[1]
                comp = "<" if "<" in r[0] else ">"
                rules.append((r0[0], comp, int(r0[1]), r[1]))
        wf[line[0]] = rules
    else:
        x, m, a, s = parse_positive_ints_str(line)
        parts.append({
            "x": x,
            "m": m,
            "a": a,
            "s": s
        })

s = 0
for part in parts:
    cur = "in"
    while cur not in ["A", "R"]:
        for rule in wf[cur]:
            if type(rule) == str:
                cur = rule
                break
            else:
                if rule[1] == "<":
                    if part[rule[0]] < rule[2]:
                        cur = rule[3]
                        break
                if rule[1] == ">":
                    if part[rule[0]] > rule[2]:
                        cur = rule[3]
                        break
    if cur == "A":
        s += sum(part.values())
print(s)