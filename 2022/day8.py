from aoc import input_as_lines, print_matrix

inp = input_as_lines("day8.txt")

N = []
for i in inp:
    N.append([int(x) for x in i])
H = len(inp)
W = len(inp[0])
moves = [(-1, 0), (0, -1), (1, 0), (0, 1)]

# PART 1
ret = 0
for col in range(1, H - 1):
    for row in range(1, W - 1):
        x = N[row][col]
        is_visible = False
        for move in moves:
            m_col = col
            m_row = row
            while not is_visible:
                m_col += move[1]
                m_row += move[0]
                if N[m_row][m_col] >= x:
                    break
                if m_col == H - 1 or m_row == W-1 or m_col == 0 or m_row == 0:
                    ret += 1
                    is_visible = True
                    break

# Add the edge trees
ret += (2*H) + (2*W) - 4
print(ret)

# PART 2
scores = []
for col in range(1, H - 1):
    for row in range(1, W - 1):
        x = N[row][col]
        distances = []
        for move in moves:
            distance = 0
            m_col = col
            m_row = row
            while True:
                m_col += move[1]
                m_row += move[0]
                distance += 1
                if N[m_row][m_col] >= x:
                    break
                if m_col == H - 1 or m_row == W-1 or m_col == 0 or m_row == 0:
                    break
            distances.append(distance)
        prod = 1
        for d in distances:
            prod *= d
        scores.append(prod)

print(max(scores))
