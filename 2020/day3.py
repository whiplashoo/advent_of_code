

def traverse(arr, dx, dy):
    trees = 0
    x = 0
    y = 0
    while True :
        #print(x, y)
        to_check = arr[y][x]
        if to_check == "#":
            trees += 1
        
        x += dx
        y += dy
        if y >= len(arr):
                break
        x = x%len(arr[y])

    return trees
        
with open("day3.txt") as f:
    
    arr = []
    for line in f:
        arr.append(line.strip())
    a = traverse(arr, 1, 1)
    b = traverse(arr, 3, 1)
    c = traverse(arr, 5, 1)
    d = traverse(arr, 7, 1)
    e = traverse(arr, 1, 2)
    print(a,b,c,d,e,)
    print(a*b*c*d*e)
    
