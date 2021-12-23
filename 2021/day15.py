from aoc import input_as_lines, print_matrix
inp = input_as_lines("day15.txt")

N = []

for line in inp:
    N.append([int(x) for x in line.strip()])

print_matrix(N)

col, row = 0, 0
visited = []


moves = [(1, 0), (0, 1)]


def dijkstra(N, start_x, start_y):
    X = len(N[0])
    Y = len(N)
    distances = [[float("inf") for col in range(X)] for row in range(Y)]
    visited = [[False for col in range(X)] for row in range(Y)]
    distances[start_x][start_y] = 0

    while True:
        shortest_distance = float("inf")
        shortest_index = (-1, -1)
        for row in range(Y):
            for col in range(X):
                if distances[row][col] < shortest_distance and not visited[row][col]:
                    shortest_distance = distances[row][col]
                    shortest_index = (row, col)
    # print("Visiting node " + str(shortest_index) + " with current distance " + str(shortest_distance))

        if shortest_index == (-1, -1):
            return distances

        for m in moves:
            move_row = shortest_index[0] + m[0]
            move_col = shortest_index[1] + m[1]
            if 0 <= move_row < Y and 0 <= move_col < X and distances[move_row][move_col] > distances[shortest_index[0]][shortest_index[1]] + N[move_row][move_col]:
                distances[move_row][move_col] = distances[shortest_index[0]
                                                          ][shortest_index[1]] + N[move_row][move_col]
        visited[shortest_index[0]][shortest_index[1]] = True


# d = dijkstra(N, 0, 0)
# print_matrix(d)
# print(d[-1][-1])
X = len(N[0])
Y = len(N)
XX = X * 5
YY = Y * 5
NN = [[0 for _ in range(XX)] for __ in range(YY)]
for row in range(YY):
    for col in range(XX):
        NN[row][col] = N[row % Y][col % X] + row//Y + col//Y
        if NN[row][col] >= 10:
            NN[row][col] -= 9
# print_matrix(NN)
d = dijkstra(NN, 0, 0)
# print_matrix(d)
print(d[-1][-1])
