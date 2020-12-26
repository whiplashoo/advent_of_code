from copy import deepcopy

adjacent = [(-1, -1), (0, -1), (1, -1), (-1, 0),
            (1, 0), (-1, 1), (0, 1), (1, 1)]


def print_matrix(matrix):
    for row in matrix:
        print("".join(row))


def part_one(seats):
    stabilized = True
    # print_matrix(seats)
    # print()
    next_seats = deepcopy(seats)
    for row in range(len(seats)):
        for col in range(len(seats[row])):
            seat = seats[row][col]
            if seat == "L":
                should_become_occupied = True
                for adj in adjacent:
                    try:
                        if row + adj[0] >= 0 and col + adj[1] >= 0:
                            if seats[row + adj[0]][col + adj[1]] == '#':
                                should_become_occupied = False
                    except IndexError:
                        continue
                if should_become_occupied:
                    stabilized = False
                    next_seats[row][col] = '#'
            if seat == '#':
                occupied_neighbors = 0
                for adj in adjacent:
                    try:
                        if row + adj[0] >= 0 and col + adj[1] >= 0:
                            if seats[row + adj[0]][col + adj[1]] == '#':
                                occupied_neighbors += 1
                    except IndexError:
                        continue
                if occupied_neighbors >= 4:
                    stabilized = False
                    next_seats[row][col] = 'L'
    if not stabilized:
        return part_one(next_seats)
    else:
        total = 0
        for row in next_seats:
            for seat in row:
                if seat == "#":
                    total += 1
        return total


def part_two(nums):
    pass


with open("day11.txt") as f:
    seats = []
    for line in f:
        seats.append([char for char in line.strip()])
    print(part_one(seats))
    # print(part_two(nums))
