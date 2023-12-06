times = [7,15,30]
records = [9,40,200]
times = [35,69,68,87]
records = [213, 1168 ,1086,1248]

times = [35696887]
records = [213116810861248]
toret = 1

ways = 0
for i, time in enumerate(times):
    speed = 0
    duration = time
    distance = 0
    for t in range(time):
        duration -= t
        speed = t
        distance = duration * speed
        if (distance > records[i]):
            ways += 1
        duration = time
    toret *= ways
    ways = 0

print(toret)

