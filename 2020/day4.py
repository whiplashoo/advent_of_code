def is_valid(passport):
    l = len(passport)
    print(l, passport)
    if l == 8 or (l == 7 and "cid" not in passport.keys()):
        return True
    return False

def is_valid2(pos1, pos2, letter, password):
    if password[pos1-1] == letter and password[pos2-1] == letter:
        return False
    if password[pos1-1] == letter or password[pos2-1] == letter:
        return True 

with open("day4.txt") as f:
    valid = 0
    lines = f.readlines()
    i = 0
    valids = 0
    passport = {}
    while i < len(lines):
        if lines[i] != "\n":
            line = lines[i].strip().split(" ")
            for prop in line:
                prop = prop.split(":")
                passport[prop[0]] = prop[1]
        else:
            if is_valid(passport):
                valids += 1
            passport = {}
        i += 1
    print(valids)
