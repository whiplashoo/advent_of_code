x_min = 169
y_min = -108
x_max = 206
y_max = -68

max_y = 0
count = 0
for i in range(0, x_max + 1):
    for j in range(y_min, -y_min + 1):
        dx, dy = i, j
        x, y = 0, 0
        while True:
            x += dx
            y += dy
            if dx > 0:
                dx -= 1
            elif dx == 0:
                dx = 0
            else:
                dx += 1
            dy -= 1
            max_y = max(y, max_y)
            if x_min <= x <= x_max and y_min <= y <= y_max:
                count += 1
                break
            if x > x_max and y > y_max:
                break
            if y < y_min:
                break
print(max_y)
print(count)
