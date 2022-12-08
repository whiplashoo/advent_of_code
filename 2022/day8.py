from aoc import input_as_lines, print_matrix

inp = input_as_lines("day8.txt")

N = []
for i in inp:
    N.append([int(x) for x in i])
H = len(inp)
W = len(inp[0])
print_matrix(N)
moves = [(-1, 0), (0, -1), (1, 0), (0, 1)]

# PART 1
ret = 0
for col in range(1, H - 1):
    for row in range(1, W - 1):
        x = N[row][col]
        #print("checking " + str(x) + " in " + str(row) + ", " + str(col))
        is_visible = False
        for move in moves:
            scol = col
            srow = row
            while not is_visible:
                scol += move[1]
                srow += move[0]
                if N[srow][scol] >= x:
                    break
                if scol == H - 1 or srow == W-1 or scol == 0 or srow == 0:
                    ret += 1
                    is_visible = True
                    break

ret += (2*H) + (2*W) - 4
print(ret)
