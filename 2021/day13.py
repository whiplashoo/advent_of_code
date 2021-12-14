from aoc import input_as_lines, print_matrix

inp = input_as_lines("day13.txt")

rows = 0
cols = 0
dots = []
folds = []
for line in inp:
    if line == "":
        continue
    if "fold" in line:
        axis = line.split("=")[0][-1]
        pos = int(line.split("=")[1])
        folds.append((axis, pos))
    else:
        col = int(line.split(",")[0])
        row = int(line.split(",")[1])
        cols = max(col, cols)
        rows = max(row, rows)
        dots.append((col, row))


print(cols, rows, dots)
print(folds)

dot_char = " "
hash_char = "█"

X = cols + 1
Y = rows + 1
N = [[dot_char for x in range(X)] for y in range(Y)]
for row in range(Y):
    for col in range(X):
        if (col, row) in dots:
            N[row][col] = hash_char


def perform_fold(P, axis, pos):
    X = len(P[0])
    Y = len(P)
    if axis == "y":
        for row in range(pos):
            for col in range(X):
                if P[row][col] == hash_char or P[Y - row - 1][col] == hash_char:
                    P[row][col] = hash_char
        return P[:pos]
    else:
        for row in range(Y):
            for col in range(pos):
                if P[row][col] == hash_char or P[row][X - col - 1] == hash_char:
                    P[row][col] = hash_char
        return [[P[row][col] for col in range(pos)] for row in range(Y)]


# PART 1
# N = perform_fold(N, folds[0][0], folds[0][1])
# count = 0
# for row in range(len(N)):
#     for col in range(len(N[0])):
#         if N[row][col] == "#":
#             count += 1
# print(count)

# PART 2
for fold in folds:
    N = perform_fold(N, fold[0], fold[1])

print_matrix(N)
