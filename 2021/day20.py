from aoc import input_as_lines, print_matrix
inp = input_as_lines("day20m.txt")

algo = inp[0]
inp_img = []
for line in inp[2:]:
    inp_img.append([x for x in line.split()])

COLS = len(inp_img[0])
ROWS = len(inp_img)
print_matrix(inp_img)
