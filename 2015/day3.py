from aoc import input_as_string


inp = input_as_string("day3.txt")

moves = { 
	"<": (-1, 0), 
	"^" : (0, -1),
	">" : (1, 0),
	"v": (0, 1)
}

visited = set()
cur = (0,0)
visited.add(cur)

for d in inp:
	cur = (cur[0] + moves[d][0], cur[1] + moves[d][1])
	visited.add(cur)

	
print(len(visited))

santa = (0,0)
robot = (0,0)

visited = set()
visited.add(robot)

santa_moving = True

for d in inp:
	if santa_moving:
		santa = (santa[0] + moves[d][0], santa[1] + moves[d][1])
		visited.add(santa)
	else:
		robot = (robot[0] + moves[d][0], robot[1] + moves[d][1])
		visited.add(robot)
	santa_moving = not santa_moving

print(len(visited))

