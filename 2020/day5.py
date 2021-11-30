def get_row(bpass):
    bpass = bpass[0:7]
    bottom = 0
    top = 2**len(bpass)
    for c in bpass:
        if c == 'F':
            top = top - (top - bottom) /2
        else:
            bottom += (top - bottom) /2
    return int(bottom) if bpass[-1] == 'F' else int(top -1)

def get_seat(bpass):
    bpass = bpass[7:]
    bottom = 0
    top = 2**len(bpass)
    for c in bpass:
        if c == 'L':
            top = top - (top - bottom) /2
        else:
            bottom += (top - bottom) /2
    return int(top-1) if bpass[-1] == 'L' else int(bottom)
    

with open("day5.txt") as f:
    max_id = 0
    arr = []

    #PART 1
    for line in f:
        line = line.strip()
        row = get_row(line)
        seat = get_seat(line)
        bpass_id = row * 8 + seat
        arr.append(bpass_id)
        if bpass_id > max_id:
            max_id = bpass_id
    print(max_id)

    #PART 2
    prev_id = arr[0]
    for b in sorted(arr)[1:]:
        if (b - prev_id == 2):
            print(b)
        else:
            prev_id = b
