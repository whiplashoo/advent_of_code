from aoc import input_as_lines

inp = input_as_lines("day8.txt")

dirs = inp[0]

nodes = {}

for line in inp[2:]:
    line = line.replace(" = (", " ").replace(",", "").replace(")", "").split(" ")
    nodes[line[0]] = (line[1], line[2])

steps = 0
# cur = "AAA"
# cur_inst = 0
# while cur!= "ZZZ":
#     inst = dirs[cur_inst % len(dirs)]
#     if inst == "L":
#         cur = nodes[cur][0]
#     else:
#         cur = nodes[cur][1]
#     cur_inst += 1
#     steps += 1

# print(steps)

#PART 2
print(nodes)

cur = []
for x in nodes.keys():
    if x.endswith("A"):
        cur.append(x)
print(cur)

def all_end_with(letter, k):
    return all([x.endswith(letter) for x in k])

dir_map = {"L": 0, "R": 1}
steps = 0
cur_inst = 0
while not all_end_with("Z", cur):
    inst = dir_map[dirs[cur_inst % len(dirs)]]
    for i in range(len(cur)):
        cur[i] = nodes[cur[i]][inst]
    cur_inst += 1
    steps+=1
    print(steps)

print(steps)
