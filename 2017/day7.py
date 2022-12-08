from aoc import input_as_lines

inp = input_as_lines("day7.txt")


class Program:
    def __init__(self, name, weight=0):
        self.name = name
        self.weight = weight
        self.parent = None

    def __repr__(self):
        return "- " + self.name + " with weight " + str(self.weight) + ".\n  -- Parent: " + str(self.parent.name if self.parent != None else "None")


# PART 1
tower = []
all_names = []
for line in inp:
    name = line.split()[0]
    w = int(line.split()[1].replace("(", "").replace(")", ""))
    program = Program(name=name, weight=w)
    tower.append(program)
    if "->" in line:
        children = line.split("-> ")[1].split(", ")
        for child in children:
            found = False
            for p in tower:
                if p.name == child:
                    p.parent = program
                    found = True
            if not found:
                tower.append(Program(name=child))

for t in tower:
    print(t)

print([t.name for t in tower])
cursor = tower[0]
while True:
    if cursor.parent == None:
        break
    cursor = cursor.parent
print(cursor.name)
