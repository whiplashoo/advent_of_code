p1 = 6
p2 = 9
s1 = 0
s2 = 0
d1 = 1
d2 = 4
n = 1

while True:
    if d1 == 101:
        d1 = 1
    if d2 == 101:
        d2 = 1
    p1 += d1
    p2 += d2
    if n % 3 == 0 and n > 0:
        s1 += p1 % 10 if p1 % 10 != 0 else 10
        if s1 > 999:
            won = 1
            break
        s2 += p2 % 10 if p2 % 10 != 0 else 10
        if s2 > 999:
            won = 2
            s1 -= p1 % 10 if p1 % 10 != 0 else 10
            break
        d1 += 4
        d2 += 4
    else:
        d1 += 1
        d2 += 1
    n += 1
    print("------")
    print(f"Turn {n}")
    print(f"p1: {p1}")
    print(f"p2: {p2}")
    print(f"s1: {s1}")
    print(f"s2: {s2}")
    print("------")


if won == 1:
    print(f"Player 1 won with {s1}")
    print(s2)
    print(s2 * d1)
else:
    print(f"Player 2 won with {s2}")
    print(s1)
    print(s1 * d2)
