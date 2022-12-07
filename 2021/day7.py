from aoc import input_as_string

inp = input_as_string("day7t.txt")


class Dir:
    def __init__(self, name):
        self.name = name
        self.size = 0
        self.parent = None
        self.dirs = []
        self.files = []

    def __repr__(self):
        return "Directory " + self.name + " with size " + self.size + ".\n  Parent: " + self.parent + ". Contains dirs: " + self.dirs + ". Contains files: " + self.files


# PART 1
folders = {"/": Dir(name="/")}
current = folders["/"]

for line in inp[1:]:
    if line.startswith("$ cd"):
        new_d = line.split()[-1]
        if new_d == "..":
            current = current.parent
        elif new_d == "/":
            current = folders["/"]
        else:
            if not folders[new_d]:
                folders[new_d] = Dir(name=new_d)
            current = folders[new_d]
    elif line.startswith("ls"):
        pass
    else:
        if line.startswith("dir"):
            new_dir = line.split()[1]
            if not folders[new_dir]:
                folders[new_dir] = Dir(name=new_dir)
                folders[new_dir].parent = current
        else:
            f = line.split()[1]
            s = int(line.split()[0])
            current.files.append(f)
            current.size += s

for f in folders:
    print(folders[f])


# PART 2
