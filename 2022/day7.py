from aoc import input_as_lines

inp = input_as_lines("day7.txt")

# Use class to represent dirs. Will probably need this again in later challenges?


class Dir:
    def __init__(self, name):
        self.name = name
        self.size = 0
        self.parent = None
        self.dirs = []
        self.files = []

    def __repr__(self):
        return "- " + self.name + " with size " + str(self.size) + ".\n  -- Parent: " + str(self.parent.name if self.parent != None else "None") + ". Dirs: " + str(self.dirs) + ". Files: " + str(self.files)


# PART 1
folders = [Dir(name="/")]
current = folders[0]

# Ignore the first line
for line in inp[1:]:
    if line.startswith("$ cd"):
        new_d = line.split()[-1]
        if new_d == "..":
            if current.parent != None:
                current = current.parent
        elif new_d == "/":
            current = folders["/"]
        else:
            new_dir = Dir(name=dir_name)
            new_dir.parent = current
            folders.append(new_dir)
            current = new_dir
    elif line.startswith("$ ls"):
        continue
    else:
        if line.startswith("dir"):
            dir_name = line.split()[1]
            current.dirs.append(dir_name)
        else:
            f = line.split()[1]
            s = int(line.split()[0])
            current.files.append(f)
            current.size += s
            cursor = current
            while cursor.parent != None:
                cursor.parent.size += s
                cursor = cursor.parent

sizes = [f.size for f in folders]
sizes_under_100000 = [s for s in sizes if s < 100000]
print(sum(sizes_under_100000))

# PART 2
total = 70000000
needed = 30000000
root_s = sizes[0]
free = total - root_s
we_need_extra = needed - free
for s in sorted(sizes):
    if s >= we_need_extra:
        print(s)
        break
